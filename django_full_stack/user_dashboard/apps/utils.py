from .dashboard_users.models import User, UserLevel

def get_logged_user(request):
  if 'userid' in request.session:
    user = User.objects.get(id=request.session['userid'])
    return user
  return None

def check_admin(logged_user):
  return logged_user is not None and logged_user.user_level == UserLevel.ADMIN.value
