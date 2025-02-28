from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from BiblioAPI.models import *
from rest_framework import viewsets,response
from BiblioAPI.serializers import *
from BiblioAPI.forms import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from .permissions import IsWallaceAdmin 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


def ajouter_livre_api(request):
    
    if request.method == 'POST':
        try:
            # Traitez les données ici
            data = json.loads(request.body)
            titre = data.get('titre')
            language = data.get('language')
            anneepulication = data.get('anneepulication')
            author = data.get('author')
            location = data.get('location')
            compartiment = data.get('compartiment')
            emplacement = data.get('emplacement')

            # Debug : afficher les données reçues
            print("Données reçues:", data)

            # Créez une instance du modèle Livre
            livre = Livre(
                titre=titre,
                langueLivre=language,
                anneepulication=anneepulication,
                author=author,
                location=location,
                compartiment=compartiment,
                emplacement=emplacement,
            )

            # Vérifiez si une image est fournie
            if 'bookImage' in request.FILES:
                livre.bookImage = request.FILES['bookImage']

            # Sauvegarder l'instance dans la base de données
            livre.save()

            return JsonResponse({'message': 'Livre ajouté avec succès!'}, status=201)

        except Exception as e:
            # Debug : afficher l'erreur
            print("Erreur lors de l'ajout du livre  dans la base de donnees :", str(e))
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)
# Create your views here.

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Ajoutez des claims personnalisés si nécessaire
        token['username'] = user.username
        return token

class EmpruntViewSet(viewsets.ModelViewSet):
    
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

class PersonneViewSet(viewsets.ModelViewSet):
    
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class EtudiantViewSet(viewsets.ModelViewSet):
    
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class LivreViewSet(viewsets.ModelViewSet):
    
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class EtrangerViewSet(viewsets.ModelViewSet):
    
    queryset = Etranger.objects.all()
    serializer_class = EtrangerSerializer

class AbonnementViewSet(viewsets.ModelViewSet):
    
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer

class EmplacementViewSet(viewsets.ModelViewSet):
    
    queryset = Emplacement.objects.all()
    serializer_class = EmplacementSerializer
    
class InscrireViewSet(viewsets.ModelViewSet):
    
    queryset = Inscrire.objects.all()
    serializer_class = InscrireSerializer

   

class EtagereViewSet(viewsets.ModelViewSet):
    
    queryset = Etagere.objects.all()
    serializer_class = EtagereSerializer

class CompartimentViewSet(viewsets.ModelViewSet):
    
    queryset = Compartiment.objects.all()
    serializer_class = CompartimentSerializer

class UniversiteViewSet(viewsets.ModelViewSet):
    
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer

class CampusViewSet(viewsets.ModelViewSet):
    
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

class FaculteViewSet(viewsets.ModelViewSet):
   
    queryset = Faculte.objects.all()
    serializer_class = FaculteSerializer

class DepartementViewSet(viewsets.ModelViewSet):
   
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    
class CountViewSet(viewsets.ModelViewSet):
    
    def get(self, request, format=None):
        Livre_count = Livre.objects.all().count()
        Etranger_count =  Etranger.objects.all().count()
        Universite_count  =  Universite.objects.all().count()
        Emprunts_count = Emprunt.objects.all().count()

        content = {
            'Livre_count': Livre_count,
            'Etranger_count':Etranger_count,
            'Universite_count':Universite_count,
            'Emprunts_count':Emprunts_count
        }
        return Response({'content': content})
    
class LoginViewSet(viewsets.ModelViewSet):
    
    def get(self, request, format=None):
            username = request.GET.get('username', False)
            password = request.GET.get('password', False)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                return Response(user)
            return Response(user)

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listelivres')  # Remplacez par la vue où vous souhaitez rediriger
    else:
        form = LivreForm()
    return render(request, 'listeLivres.html', {'form': form})
"""la classe pour enregistrer une etagere dans le systeme"""
