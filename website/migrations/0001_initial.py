# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom_commercial', models.CharField(max_length=20)),
                ('nom_generique', models.CharField(max_length=30)),
                ('composition', models.CharField(max_length=100)),
                ('forme_gallenique', models.CharField(max_length=50)),
                ('dosage', models.CharField(blank=True, max_length=100, null=True)),
                ('quantite', models.CharField(max_length=30)),
                ('compagnie', models.CharField(max_length=15)),
                ('Agence', models.ForeignKey(to='website.Agence')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=16)),
                ('adresse', models.CharField(max_length=200)),
                ('zone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='medicament',
            name='disponibilite',
            field=models.ManyToManyField(to='website.Pharmacie'),
        ),
        migrations.AddField(
            model_name='agence',
            name='distrib',
            field=models.ManyToManyField(to='website.Medicament'),
        ),
    ]
