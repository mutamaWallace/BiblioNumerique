from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BiblioApp.views import *
from .views import * 

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
    # #  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #   path('api/', include('rest_framework.urls')),
    path('prod/count/', CountViewSet.as_view({'get': 'content'}), name='produits-count')
   
]