from django.shortcuts import render, redirect
from django.db.models import Q, Count
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
#		"leagues": League.objects.filter(name__contains='Atlantic'),
#		PART TWO
#		"leagues": League.objects.filter(name__contains='Atlantic'),
		"leagues": League.objects.filter(teams__curr_players__first_name='Sophia'),
#		"teams": Team.objects.all(),
#		"teams": Team.objects.filter(location='Dallas'),
#		"teams": Team.objects.filter(team_name='Raptors'),
#		"teams": Team.objects.filter(location__contains='City'),
#		"teams": Team.objects.filter(team_name__startswith='T'),
#		"teams": Team.objects.all().order_by('location'),
#		"teams": Team.objects.all().order_by('-team_name'),
#		PART TWO
#		"teams": Team.objects.filter(league__name='Atlantic Soccer Conference'),
#		"teams": Team.objects.filter(curr_players__first_name='Sophia'),
#		"teams": Team.objects.filter(Q(all_players__first_name='Samuel') & Q(all_players__last_name='Evans')),
#		"teams": Team.objects.filter(Q(all_players__first_name='Jacob') & Q(all_players__last_name='Gray') & ~(Q(team_name='Colts') & Q(location='Oregon'))),
		"teams": Team.objects.annotate(count=Count('all_players')).filter(count__gt=12),
#		"players": Player.objects.all(),
#		"players": Player.objects.filter(last_name='Cooper'),
#		"players": Player.objects.filter(Q(last_name='Cooper') & ~Q(first_name='Joshua')),
#		"players": Player.objects.filter(Q(first_name='Alexander') | Q(first_name='Wyatt')),
#		PART TWO
#		"players": Player.objects.filter(Q(curr_team__team_name='Penguins') & Q(curr_team__location='Boston')),
#		"players": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference'),
#		"players": Player.objects.filter(Q(curr_team__league__name='American Conference of Amateur Football') & Q(last_name='Lopez')),
#		"players": Player.objects.filter(curr_team__league__sport='Football'),
#		"players": Player.objects.filter(curr_team__league__sport='Football'),
#		"players": Player.objects.filter(Q(last_name='Flores') & ~(Q(curr_team__team_name='Roughriders') & Q(curr_team__location='Washington'))),
#		"players": Player.objects.filter(Q(all_teams__team_name='Tiger-Cats') & Q(all_teams__location='Manitoba')),
#		"players": Player.objects.filter((Q(all_teams__team_name='Vikings') & Q(all_teams__location='Wichita')) & ~(Q(curr_team__team_name='Vikings') & Q(curr_team__location='Wichita'))),
#		"players": Player.objects.filter(Q(all_teams__league__name='Atlantic Federation of Amateur Baseball Players') & Q(first_name='Joshua')),
		"players": Player.objects.all().annotate(nbr_of_teams=Count('all_teams')).order_by('-nbr_of_teams'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")