from django.shortcuts import render, redirect
from django.db.models import Q
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
#		"leagues": League.objects.all(),
#		"leagues": League.objects.filter(sport='Baseball'),
#		"leagues": League.objects.filter(name__contains='Women'),
#		"leagues": League.objects.filter(sport__contains='Hockey'),
#		"leagues": League.objects.exclude(sport='Football'),
#		"leagues": League.objects.filter(name__contains='Conference'),
		"leagues": League.objects.filter(name__contains='Atlantic'),
#		"teams": Team.objects.all(),
#		"teams": Team.objects.filter(location='Dallas'),
#		"teams": Team.objects.filter(team_name='Raptors'),
#		"teams": Team.objects.filter(location__contains='City'),
#		"teams": Team.objects.filter(team_name__startswith='T'),
#		"teams": Team.objects.all().order_by('location'),
		"teams": Team.objects.all().order_by('-team_name'),
#		"players": Player.objects.all(),
#		"players": Player.objects.filter(last_name='Cooper'),
#		"players": Player.objects.filter(Q(last_name='Cooper') & ~Q(first_name='Joshua')),
		"players": Player.objects.filter(Q(first_name='Alexander') | Q(first_name='Wyatt')),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")