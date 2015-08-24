# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Sujet', models.CharField(max_length=255)),
                ('Contenu', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Autheur',
            field=models.ForeignKey(to='pharmablog.Author'),
        ),
    ]
