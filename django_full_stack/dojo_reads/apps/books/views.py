from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.login.models import User
from .models import Author, Book, Review
from django.contrib import messages
from django.db.models import Avg, Count, Sum


@require_http_methods(['GET'])
def index(request):
    if 'userid' not in request.session:
        redirect('/')

    context = {
        'user': User.objects.get(id=request.session['userid']),
        'books': Book.objects.annotate(
            avg_review=Avg('reviews__rating'),
            total_reviews=Sum('reviews')
        ).all().order_by('-created_at'),
        'rating_choices': Review._meta.get_field('rating').choices,
    }
    return render(request, 'books.html', context)


@require_http_methods(['GET'])
def books_add(request):
    if 'userid' not in request.session:
        redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'authors': Author.objects.all(),
        'rating_choices': Review._meta.get_field('rating').choices,
    }
    return render(request, 'books_add.html', context)

@require_http_methods(['POST'])
def books_create(request):
    if 'userid' not in request.session:
        return redirect('/')
    for m in [Book, Author, Review]:
        errors = m.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
    else:
        title = request.POST['title_input']
        review = request.POST['review_input']
        rating = request.POST['rating_select']
        selected_author = int(request.POST['author_select'])
        if selected_author != 0:
            author = Author.objects.get(id=selected_author)
        else:
            author_name = request.POST['author_input']
            author = Author.objects.create(name=author_name)
        user = User.objects.get(id=request.session['userid'])
        book = Book.objects.create(
            title=title, author=author, uploaded_by=user)
        review = Review.objects.create(
            review=review, rating=rating, book=book, posted_by=user)
        return redirect('book', id=book.id)
    return redirect('/')

@require_http_methods(['GET'])
def book(request, id: int):
    if 'userid' not in request.session:
        redirect('/')
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)
    context = {
        'user': user,
        'book': book,
        'books_reviewed': [r.book for r in user.reviews.all()],
        'rating_choices': Review._meta.get_field('rating').choices,
    }
    return render(request, 'book.html', context=context)

@require_http_methods(['POST'])
def book_destroy(request, id: int):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)
    if book.uploaded_by == user:
        book.delete()
    return redirect('books')

@require_http_methods(['POST'])
def review_create(request, id:int):
    if 'userid' not in request.session:
        return redirect('/')
    errors = Review.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        review = request.POST['review_input']
        rating = request.POST['rating_select']
        user = User.objects.get(id=request.session['userid'])
        book = Book.objects.get(id=id)
        review = Review.objects.create(
            review=review, rating=rating, book=book, posted_by=user)
        return redirect('book', id=id)
    return redirect('/')

@require_http_methods(['POST'])
def review_destroy(request, id: int, review_id:int):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    review = Review.objects.get(id=review_id)
    if review.posted_by == user:
        review.delete()
    return redirect('book', id=id)

@require_http_methods(['GET'])
def user(request, id: int):
    if 'userid' not in request.session:
        redirect('/')
    user = User.objects.get(id=request.session['userid'])
    usr = User.objects.annotate(
      total_reviews=Count('reviews')
    ).get(id=id)
    context = {
        'user': user,
        'usr': usr,
    }
    return render(request, 'user.html', context=context)
