"""
URL configuration for BibliothequeNumerique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from BiblioApp.views import *
from django.contrib import admin
from BiblioAPI.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('profile/', LoginView.as_view(), name='profile'),
    path('login2/', LoginView.as_view(), name='login2'),
    path('liste_bibliothecaires/', liste_bibliothecaires, name = 'liste_bibliotecaires'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboardPersonnel/', DashboardPersonnelView.as_view(), name='dashboardPersonnel'), 
    path('ajouter_livre/', ajouter_livre, name='ajouter_livre'),
    path('liste_livres/', liste_livres, name='liste_livres'),
    # path('etagere/', EtagereCreateView.as_view(), name='etagere'),
    # path('compartiment/', ajouter_compartiment, name='compartiment'),
    # path('', ProfileView.as_view()),
    # path('', profile_view, name='profile'),
    # path('profile/', profile_view, name='profile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('prod/count', CountViewSet.as_view({'get': 'list'}), name='produits-count'),
    path('statistiques/', StatistiqueView.as_view(), name='statistiques'),
]

