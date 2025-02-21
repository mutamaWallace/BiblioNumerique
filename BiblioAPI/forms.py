from django import forms
from .models import *

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'username', 'password', 'genre', 'profil', 'tel', 'matricule', 'datenaissance', 'CNI']
        widgets = {
            'password': forms.PasswordInput(),
        }

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'username', 'password', 'genre', 'photo_passport', 'datenaissance']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom']

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'langueLivre', 'annee_publication', 'imagelivre', 'auteur', 'id_emplacement', 'compartiment', 'etagere']

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Abonnement
        fields = ['type_abonnement', 'date_debut', 'date_fin']

class EtrangerForm(forms.ModelForm):
    class Meta:
        model = Etranger
        fields = ['nom', 'prenom', 'email', 'username', 'password', 'genre', 'photo_passport', 'datenaissance', 'CNI', 'abonnement']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['campus', 'code']

class UniversiteForm(forms.ModelForm):
    class Meta:
        model = Universite
        fields = ['nom', 'pays', 'ville', 'email', 'site_web', 'id_campus']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['date_emprunt', 'date_retour', 'id_etudiant', 'id_etrangere', 'id_personne', 'id_livre', 'rendu']

class FaculteForm(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['faculte', 'id_universite']

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['departement', 'id_faculte']

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['niveau', 'id_departement']

class InscrireForm(forms.ModelForm):
    class Meta:
        model = Inscrire
        fields = ['date_inscrit', 'date_fin_inscrit', 'type_inscrition', 'etudiant', 'universite', 'faculte', 'departement', 'classe']