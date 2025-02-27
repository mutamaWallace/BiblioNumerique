# Generated by Django 5.1.6 on 2025-02-28 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BiblioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etranger',
            name='abonnement',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='universite',
            name='id_campus',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='id_departement',
        ),
        migrations.RemoveField(
            model_name='inscrire',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='compartiment',
            name='etagere',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='compartiment',
        ),
        migrations.RemoveField(
            model_name='departement',
            name='id_faculte',
        ),
        migrations.RemoveField(
            model_name='inscrire',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='id_emplacement',
        ),
        migrations.RemoveField(
            model_name='emprunt',
            name='id_etrangere',
        ),
        migrations.RemoveField(
            model_name='emprunt',
            name='id_etudiant',
        ),
        migrations.RemoveField(
            model_name='emprunt',
            name='id_livre',
        ),
        migrations.RemoveField(
            model_name='emprunt',
            name='id_personne',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='etagere',
        ),
        migrations.RemoveField(
            model_name='inscrire',
            name='etudiant',
        ),
        migrations.RemoveField(
            model_name='faculte',
            name='id_universite',
        ),
        migrations.RemoveField(
            model_name='inscrire',
            name='faculte',
        ),
        migrations.RemoveField(
            model_name='inscrire',
            name='universite',
        ),
        migrations.DeleteModel(
            name='Abonnement',
        ),
        migrations.DeleteModel(
            name='Auteur',
        ),
        migrations.DeleteModel(
            name='Campus',
        ),
        migrations.DeleteModel(
            name='Classe',
        ),
        migrations.DeleteModel(
            name='Compartiment',
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Emplacement',
        ),
        migrations.DeleteModel(
            name='Etranger',
        ),
        migrations.DeleteModel(
            name='Emprunt',
        ),
        migrations.DeleteModel(
            name='Personne',
        ),
        migrations.DeleteModel(
            name='Etagere',
        ),
        migrations.DeleteModel(
            name='Livre',
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
        migrations.DeleteModel(
            name='Faculte',
        ),
        migrations.DeleteModel(
            name='Inscrire',
        ),
        migrations.DeleteModel(
            name='Universite',
        ),
    ]
