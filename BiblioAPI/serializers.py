from rest_framework import serializers
from .models import *

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'

class EtrangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etranger
        fields = '__all__'

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class UniversiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universite
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'

class FaculteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculte
        fields = '__all__'

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class InscrireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrire
        fields = '__all__'
        


class EmplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emplacement
        fields = '__all__'
        

class EtagereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etagere
        fields = '__all__'
        
class CompartimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartiment
        fields = '__all__'
        