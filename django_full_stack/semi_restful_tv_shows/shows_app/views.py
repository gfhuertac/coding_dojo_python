from django.shortcuts import render, HttpResponseRedirect, resolve_url
from django.views.decorators.http import require_http_methods

from datetime import datetime

from . import models

@require_http_methods(['GET'])
def shows(request):
  context = { 'shows': models.Show.objects.all() }
  return render(request, 'shows/index.html', context=context)

@require_http_methods(['GET'])
def shows_new(request):
  return render(request, 'shows/new.html')

@require_http_methods(['POST'])
def shows_create(request):
  title = request.POST['title_input']
  network = request.POST['network_input']
  release_date = datetime.strptime(request.POST['release_date_input'], '%B %d, %Y')
  description = request.POST['description_input']
  show = models.Show.objects.create(
    title=title,
    network=network,
    release_date=release_date,
    description=description
  )
  return HttpResponseRedirect(resolve_url('show', id=show.id))

@require_http_methods(['GET'])
def show(request, id:int):
  show = models.Show.objects.get(id=id)
  return render(request, 'shows/show.html', context={'show': show})

@require_http_methods(['GET'])
def show_edit(request, id:int):
  show = models.Show.objects.get(id=id)
  return render(request, 'shows/edit.html', context={'show': show})

@require_http_methods(['POST'])
def show_update(request, id:int):
  show = models.Show.objects.get(id=id)
  show.title = request.POST['title_input']
  show.network = request.POST['network_input']
  show.release_date = datetime.strptime(request.POST['release_date_input'], '%B %d, %Y')
  show.description = request.POST['description_input']
  show.save()
  return HttpResponseRedirect(resolve_url('show', id=show.id))

@require_http_methods(['POST'])
def show_destroy(request, id:int):
  show = models.Show.objects.get(id=id)
  show.delete()
  return HttpResponseRedirect(resolve_url('shows'))
