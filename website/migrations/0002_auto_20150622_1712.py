# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agence',
            name='distrib',
            field=models.ManyToManyField(null=True, blank=True, to='website.Medicament'),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='Agence',
            field=models.ForeignKey(null=True, to='website.Agence', blank=True),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='disponibilite',
            field=models.ManyToManyField(null=True, blank=True, to='website.Pharmacie'),
        ),
        migrations.AlterField(
            model_name='pharmacie',
            name='zone',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
    ]
