"""pl_players_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from api.views import (home, 
                        update_models , 
                        Documentation,
                        PlayerInfoList,
                        PlayerSeasonWiseStatsList,
                        PlayerAttackingStatsList,
                        PlayerDefensiveStatsList,
                        PlayerDisciplinaryStatsList,
                        PlayerTeamPlayStatsList,
                        PlayerGoalKeepingStatsList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login', auth_views.LoginView.as_view(template_name = 'api/login.html')),
    path('player_info/', PlayerInfoList.as_view(), name="player-info"),
    path('update_db/',update_models, name="update-database"),
    path('docs/', Documentation.as_view(), name= "docs"),
    path('player_attacking_stats/', PlayerAttackingStatsList.as_view(), name="plasyer-attacking_stat"),
    path('player_defensive_stats/', PlayerDefensiveStatsList.as_view(), name="plasyer-defensive-stat"),
    path('player_disciplinary_stats/', PlayerDisciplinaryStatsList.as_view() , name="player-disciplinary-stat"),
    path('player_teamplay_stats/', PlayerTeamPlayStatsList.as_view(), name="player-teamplay-stat"),
    path('player_goalkeeping_stats/', PlayerGoalKeepingStatsList, name="player-goalkeeping-stat"),
]
