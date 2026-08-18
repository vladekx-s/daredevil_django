from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page),
    path('player/', views.get_player_page),
    path('wiki/', views.get_wiki_page),
    path('profile/', views.get_profile_page),
]