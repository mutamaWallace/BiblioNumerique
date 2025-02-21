from django.contrib import admin
from .models import *

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email', 'username', 'genre', 'tel', 'matricule', 'datenaissance', 'CNI')
    search_fields = ('nom', 'prenom', 'email', 'username', 'matricule', 'CNI')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email', 'username', 'genre', 'datenaissance')
    search_fields = ('nom', 'prenom', 'email', 'username')

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom')
    search_fields = ('nom', 'prenom')

@admin.register(Emplacement)
class EmplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero')
    search_fields = ('numero',)

@admin.register(Etagere)
class EtagereAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'etat_etagere', 'mobilite', 'charge_maximal')
    search_fields = ('nom',)

@admin.register(Compartiment)
class CompartimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'nombreLivre', 'domaineLivre', 'etagere')
    search_fields = ('nom',)

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'langueLivre', 'annee_publication','auteur', 'id_emplacement', 'compartiment', 'etagere')
    search_fields = ('titre', 'auteur__nom', 'langueLivre')

@admin.register(Abonnement)
class AbonnementAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_abonnement', 'date_debut', 'date_fin')
    search_fields = ('type_abonnement',)

@admin.register(Etranger)
class EtrangerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email', 'username', 'genre', 'CNI')
    search_fields = ('nom', 'prenom', 'email', 'username')

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'campus', 'code')
    search_fields = ('campus',)

@admin.register(Universite)
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'pays', 'ville', 'email', 'site_web')
    search_fields = ('nom', 'pays', 'ville')

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_emprunt', 'date_retour', 'id_etudiant', 'id_etrangere', 'id_personne', 'id_livre', 'rendu')
    search_fields = ('id_etudiant__prenom', 'id_livre__titre')

@admin.register(Faculte)
class FaculteAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculte', 'id_universite')
    search_fields = ('faculte',)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('id', 'departement', 'id_faculte')
    search_fields = ('departement',)

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id', 'niveau', 'id_departement')
    search_fields = ('niveau',)

@admin.register(Inscrire)
class InscrireAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_inscrit', 'date_fin_inscrit', 'type_inscrition', 'etudiant', 'universite', 'faculte', 'departement', 'classe')
    search_fields = ('etudiant__prenom', 'universite__nom')