from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BiblioApp.views import *
from .views import * 
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from BiblioAPI.views import  CustomTokenObtainPairSerializer

router = DefaultRouter()

router.register('emprunts', EmpruntViewSet)
router.register('personnes', PersonneViewSet)
router.register('etudiants', EtudiantViewSet)
router.register('auteurs', AuteurViewSet)
router.register('lives', LivreViewSet)
router.register('inscrire', InscrireViewSet) 
router.register('etrangers', EtrangerViewSet)
router.register('abonnements', AbonnementViewSet)
router.register('emplacements', EmplacementViewSet)
router.register('etageres', EtagereViewSet)
router.register('compartiments', CompartimentViewSet)
router.register('universites', UniversiteViewSet)
router.register('campus', CampusViewSet)
router.register('facultes', FaculteViewSet)
router.register('departements', DepartementViewSet)
router.register('classes', ClasseViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('prod/count', CountViewSet.as_view({'get': 'content'}), name='produits-count'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/', include('rest_framework.urls')),
    # path('ajouter_livre/', ajouter_livre, name = 'ajouter_livre'),
    path('ajouter_livre_api/', ajouter_livre_api, name='ajouter_livre_api'),
    path('prod/count/', CountViewSet.as_view({'get': 'content'}), name='produits-count')
   
]