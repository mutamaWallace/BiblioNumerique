from django .shortcuts import render, redirect
from BiblioApp import *  
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import messages
from BiblioAPI.forms import *


class LoginView(TemplateView):
    template_name = 'login2.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # Redirection basée sur le rôle de l'utilisateur
            if user.is_superuser:  # Vérifiez si c'est un super utilisateur
                return redirect('admin:index')  # Redirigez vers le tableau de bord admin
            elif user.role == 'simple':  # Adaptez ce champ selon votre modèle
                return redirect('livres')  # Redirigez vers la page des livres
            return redirect('dashboardPersonnel')  # Autres utilisateurs

        messages.error(request, 'Mot de passe ou nom d\'utilisateur incorrect')
        return render(request, self.template_name)

class LogoutView(TemplateView):
    template_name = 'logout.html'
    
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
class DashboardPersonnelView(TemplateView):
    template_name = 'dashboardPersonnel.html'    # Assure-toi que ce fichier existe dans templates
    
    
# class ProfileView(TemplateView):
#     template_name = 'profile.html'  # Remplace par le chemin de ton template

def profile_view(request):
    # Logique pour récupérer les données de profil de l'utilisateur
    return render(request, 'accounts/profile.html')


def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listelivres')  # Remplacez par la vue où vous souhaitez rediriger
    else:
        form = LivreForm()
    return render(request, 'listeLivres.html', {'form': form})





def ajouter_bibliothecaire(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bibliothecaire')  # Remplacez par la vue où vous souhaitez rediriger
    else:
        form = PersonneForm()
    return render(request, 'bibliothecaire.html', {'form': form})




def ajouter_etrangere(request):
    if request.method == 'POST':
        form = EtrangerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('etrangere')  # Remplacez par la vue où vous souhaitez rediriger
    else:
        form = EtrangerForm()
    return render(request, 'etrangere.html', {'form': form})






"""la classe pour enregistrer une etagere dans le systeme"""

# class EtagereCreateView(TemplateView):
#     def get(self, request):
#         form = EtagereForm()
#         return render(request, 'etagere.html', {'form': form})

#     def post(self, request):
#         form = EtagereForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('etagere.html')  # Remplacez par le nom de votre URL de succès
#         return render(request, 'etagere.html', {'form': form})
    
    
# def ajouter_compartiment(request):
#     if request.method == 'POST':
#         form = CompartimentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # Enregistrer l'objet Livre dans la base de données
#             return redirect('compartiment')  # Rediriger après le succès
#     else:
#         form = LivreForm()  # Créer une instance vide du formulaire pour GET

#     return render(request, 'compartiment.html', {'form': form})
    
def liste_livres(request):
    livres = Livre.objects.all()  # Récupère tous les livres
    auteurs = Auteur.objects.all()
    etageres = Etagere.objects.all()
    compartiments = Compartiment.objects.all()
    emplacements = Emplacement.objects.all()
    
    content = {
        'livres':livres,
        'auteurs':auteurs,
         'etageres':etageres,
        'compartiments':compartiments,
        'emplacements':emplacements,
    }
    return render(request, 'listelivres.html', content)

def liste_bibliothecaires(request):
    bibliothecaires = Personne.objects.all()
    
    return render(request, 'bibliothecaire.html', {'bibliothecaires': bibliothecaires})



def liste_etrangeres(request):
    etrangeres = Etranger.objects.all() 
    abonnements = Abonnement.objects.all() 
    content = {
        'etrangeres':etrangeres,
        'abonnements':abonnements,
    
    }
    

    return render(request, 'etrangere.html', {'etrangeres': etrangeres})

def liste_universites(request):
    universites = Universite.objects.all() 
    campus = Campus.objects.all() 
    content = {
        'universites':universites,
        'campus':campus,
    
    }
    

    return render(request, 'partenaire.html', {'content': content})




def liste_emprunts(request):
    emprunts = Emprunt.objects.all() 
    personnes = Personne.objects.all() 
    livres = Livre.objects.all()
    etudiants = Etudiant.objects.all()
    etrangeres =Etranger.objects.all()
    context = {
        'emprunts': emprunts,
        'personnes':personnes,
         'livres': livres,
         'etudiants': etudiants,
         'etrangeres':etrangeres
             
    }
    

    return render(request, 'emprunts.html', {'context': context})



class StatistiqueView(TemplateView):
    def get(self, request, format=None):
        Livre_count = Livre.objects.all().count()
        Etranger_count =  Etranger.objects.all().count()
        Universite_count  =  Universite.objects.all().count()
        Emprunts_count = Emprunt.objects.all().count()

        context = {
            'Livre_count': Livre_count,
            'Etranger_count':Etranger_count,
            'Universite_count':Universite_count,
            'Emprunts_count':Emprunts_count
        }
        return render(request, 'statistiques.html', context)


