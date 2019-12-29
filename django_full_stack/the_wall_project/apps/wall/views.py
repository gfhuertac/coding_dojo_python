from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.login.models import User
from .models import Message, Comment

@require_http_methods(['GET'])
def index(request):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  messages = Message.objects.all()
  context = {
    'user': user,
    'messages': messages,
  }
  return render(request, 'wall.html', context)

@require_http_methods(['POST'])
def create_message(request):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  message=request.POST['message_input']
  message = Message.objects.create(message=message, user=user)
  return redirect('wall')

@require_http_methods(['POST'])
def delete_message(request, id:int):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  message = Message.objects.get(id=id)
  if message.user.id == user.id:
    message.delete()
  return redirect('wall')

@require_http_methods(['POST'])
def create_comment(request, message_id:int):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  message = Message.objects.get(id=message_id)
  comment = request.POST['comment_input']
  comment = Comment.objects.create(comment=comment, message=message, user=user)
  return redirect('wall')

@require_http_methods(['POST'])
def delete_comment(request, message_id:int, id:int):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  comment = Comment.objects.get(id=id)
  if comment.user.id == user.id:
    comment.delete()
  return redirect('wall')