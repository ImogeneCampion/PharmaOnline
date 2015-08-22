# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150713_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('pays_origine', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='medicament',
            name='compagnie',
            field=models.ForeignKey(blank=True, to='website.Compagnie', null=True),
        ),
    ]
