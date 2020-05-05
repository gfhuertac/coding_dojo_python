import bcrypt

from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .models import User, UserRole, Loan
from django.http import HttpResponse

def get_logged_user(request):
  """
      Method to get the currently logged user
    Args:
      - request (HttpRequest): the request
    Returns:
    The currently logged user if any, None otherwise
  """
  if 'userid' in request.session:
    user = User.objects.get(id=request.session['userid'])
    return user
  return None

def redirects_by_role(user):
  """
    Method to redirect to the page based on the role
    Args:
      - user (User): the logged in user
    Returns:
    A redirection to borrower if user role is borrower, lender otherwise
  """
  if user.user_role == UserRole.BORROWER:
    return redirect('borrower', id=user.id)
  elif user.user_role == UserRole.LENDER:
    return redirect('lender', id=user.id)

@require_GET
def index(request):
  """
    Root view. Currently it redirects to the register view.
  """
  return redirect('/register')

@require_GET
def register(request):
  """
    Register view.
    It displays the registration webpage.
    Args:
      - request (HttpRequest): the request
    Returns:
  """
  context = {
    'borrower_role': UserRole.BORROWER,
    'lender_role': UserRole.LENDER,
    'initial': request.session.get('form_data', {})
  }
  return render(request, 'register.html', context)

@require_GET
def login(request):
  """
    Login view.
    It displays the login webpage.
    Args:
      - request (HttpRequest): the request
    Returns:
  """
  return render(request, 'login.html')

@require_GET
def logout(request):
  """
    Logout view.
    It clears the session and redirects to the root view.
  """
  request.session.clear()
  return redirect('/')

@require_POST
def user_create(request):
  """
    User creation view.
    It receives the data from the registration webpage, process and validates it,
    and creates a user if everything is OK
    Args:
      - request (HttpRequest): the request
    Returns:
  """
  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    request.session['form_data'] = {k:v for k,v in request.POST.items()}
    print('RS', request.session['form_data'])
    for key, value in errors.items():
      messages.error(request, value)
      del request.session['form_data'][key]
    return redirect('register')
  else:
    first_name = request.POST.get('first_name_input', '')
    last_name = request.POST.get('last_name_input', '')
    email = request.POST.get('email_input', '')
    password = request.POST.get('password_input', '')
    money = request.POST.get('money_input', 0)
    need_money_for = request.POST.get('need_money_for_input', '')
    description = request.POST.get('description_input', '')
    user_role = int(request.POST.get('user_role_input', UserRole.GUEST))

    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
      first_name=first_name,
      last_name=last_name,
      email=email,
      password=pw_hash,
      money=money,
      need_money_for=need_money_for,
      description=description,
      user_role=user_role
    )
    request.session['userid'] = new_user.id
    return redirects_by_role(new_user)

@require_POST
def user_check(request):
  """
    User login view.
    It receives the data from the login webpage, process and validates it,
    and redirects the user if everything is OK
    Args:
      - request (HttpRequest): the request
    Returns:
  """
  email = request.POST.get('email_input', '')
  password = request.POST.get('password_input', '')
  user = User.objects.filter(email=email)
  if user and len(user) == 1:
    logged_user = user[0]
    if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
      request.session['userid'] = logged_user.id
      return redirects_by_role(logged_user)
  messages.error(request, 'Invalid username or password')
  return redirect('login')

@require_GET
def borrower(request, id):
  """
    Borrower view.
    It displays the borrower view, containing the profile and list of people who lend money to her/him
    Args:
      - request (HttpRequest): the request
      - id (int): the user id
    Returns:
  """
  logged_user = get_logged_user(request)
  if logged_user is not None and logged_user.id == id and logged_user.user_role == UserRole.BORROWER:
    consolidated_debts = {}
    for debt in logged_user.debts.all():
      d = dict(debt.lender.__dict__)
      d['amount'] = 0
      consolidated_debt = consolidated_debts.get(debt.lender.email, d)
      consolidated_debt['amount'] += debt.amount
      consolidated_debts[debt.lender.email] = consolidated_debt
    context = {
      'logged_user': logged_user,
      'debts': consolidated_debts.values()
    }
    return render(request, 'borrower.html', context)
  else:
    request.session.clear()
    return redirect('/')

@require_GET
def lender(request, id):
  """
    Lender view.
    It displays the lender view, containing the profile, the list of people
    in need (if balance is positive) and list of people who owes money to her/him
    Args:
      - request (HttpRequest): the request
      - id (int): the user id
    Returns:
  """
  logged_user = get_logged_user(request)
  if logged_user is not None and logged_user.id == id and logged_user.user_role == UserRole.LENDER:
    borrowers = User.objects.filter(user_role=UserRole.BORROWER)
    open_requests = []
    for borrower in borrowers:
      if borrower.borrowed_amount < borrower.money:
        d = dict(borrower.__dict__)
        d['borrowed_amount'] = borrower.borrowed_amount
        open_requests.append(d)
    consolidated_loans = {}
    for loan in logged_user.loans.all():
      d = dict(loan.borrower.__dict__)
      d['borrowed_amount'] = loan.borrower.borrowed_amount
      d['amount'] = 0
      consolidated_loan = consolidated_loans.get(loan.borrower.email, d)
      consolidated_loan['amount'] += loan.amount
      consolidated_loans[loan.borrower.email] = consolidated_loan
    context = {
      'logged_user': logged_user,
      'balance': logged_user.money - logged_user.lent_amount,
      'loans': consolidated_loans.values(),
      'open_requests': open_requests
    }
    return render(request, 'lender.html', context)
  else:
    request.session.clear()
    return redirect('/')

@require_POST
def lend(request):
  """
    Lend view.
    It receives the data from the lend form, process and validates it,
    and reloads the page if everything is OK
    Args:
      - request (HttpRequest): the request
    Returns:
  """
  logged_user = get_logged_user(request)
  if logged_user is not None and logged_user.user_role == UserRole.LENDER:
    d = dict(request.POST)
    d['lender_input'] = logged_user.id
    errors = Loan.objects.basic_validator(d)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
    else:
      borrower = request.POST.get('borrower_input', 0)
      amount = request.POST.get('amount_input', 0)
      new_loan = Loan.objects.create(
        borrower=User.objects.get(id=borrower),
        lender=logged_user,
        amount=int(amount)
      )
      messages.info(request, 'Loan executed successfully')
    return redirect('lender', id=logged_user.id)
  else:
    request.session.clear()
    return redirect('/')


