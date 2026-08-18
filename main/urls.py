from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    
    path('player/<int:season>/<int:episode>', views.player_page, name='player'),
    
    path('wiki/', views.wiki_page),
    
    path('profile/', views.profile_page, name='profile'),
    
    path('login/', views.login_user, name='login'),
    
    path('logout/', views.logout_user, name='logout'),
    
    path('registration/', views.registration_user, name='registration'),
]
