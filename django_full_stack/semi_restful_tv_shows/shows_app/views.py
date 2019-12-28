from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, resolve_url
from django.views.decorators.http import require_http_methods

from datetime import datetime

from .models import Show

@require_http_methods(['GET'])
def shows(request):
  context = { 'shows': Show.objects.all() }
  return render(request, 'shows/index.html', context=context)

@require_http_methods(['GET'])
def shows_new(request):
  return render(request, 'shows/new.html')

@require_http_methods(['POST'])
def shows_create(request):
  errors = Show.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return HttpResponseRedirect(resolve_url('shows_new'))
  else:
    title = request.POST['title_input']
    network = request.POST['network_input']
    release_date = datetime.strptime(request.POST['release_date_input'], '%B %d, %Y')
    description = request.POST['description_input']
    show = Show.objects.create(
      title=title,
      network=network,
      release_date=release_date,
      description=description
    )
    return HttpResponseRedirect(resolve_url('show', id=show.id))

@require_http_methods(['GET'])
def show(request, id:int):
  show = Show.objects.get(id=id)
  return render(request, 'shows/show.html', context={'show': show})

@require_http_methods(['GET'])
def show_edit(request, id:int):
  show = Show.objects.get(id=id)
  return render(request, 'shows/edit.html', context={'show': show})

@require_http_methods(['POST'])
def show_update(request, id:int):
  errors = Show.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return HttpResponseRedirect(resolve_url('shows_new'))
  else:
    show = Show.objects.get(id=id)
    show.title = request.POST['title_input']
    show.network = request.POST['network_input']
    show.release_date = datetime.strptime(request.POST['release_date_input'], '%B %d, %Y')
    show.description = request.POST['description_input']
    show.save()
    return HttpResponseRedirect(resolve_url('show', id=show.id))

@require_http_methods(['POST'])
def show_destroy(request, id:int):
  show = Show.objects.get(id=id)
  show.delete()
  return HttpResponseRedirect(resolve_url('shows'))
