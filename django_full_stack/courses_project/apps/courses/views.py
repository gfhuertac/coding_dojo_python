from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Course, Comment, Description

# Create your views here.
def index(request):
  if request.method == 'POST':
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
    else:
      description = request.POST['description_input']
      description = Description.objects.create(description=description)
      name = request.POST['name_input']
      course = Course.objects.create(name=name, description=description)
      return redirect('/')
  context = {
    'courses': Course.objects.all()
  }
  return render(request, 'courses/index.html', context)

def destroy(request, id:int):
  course = Course.objects.get(id=id)
  if request.method == 'POST':
    course.delete()
    return redirect('/')
  context = {
    'course': course
  }
  return render(request, 'courses/destroy.html', context)

def comments(request, id:int):
  if request.method == 'POST':
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
    else:
      content = request.POST['content_input']
      course = Course.objects.get(id=id)
      Comment.objects.create(content=content, course=course)
      return redirect('course_comments', id=id)
  context = {
    'comments': Comment.objects.filter(course__id=id)
  }
  return render(request, 'courses/comments.html', context)
