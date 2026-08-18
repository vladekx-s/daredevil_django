from django.shortcuts import render

# Create your views here.
def get_home_page(request):
    return render(request, "home.html")


def get_wiki_page(request):
    return render(request, "wiki.html")


def get_player_page(request):
    return render(request, "player.html")


def get_profile_page(request):
    return render(request, "profile.html")