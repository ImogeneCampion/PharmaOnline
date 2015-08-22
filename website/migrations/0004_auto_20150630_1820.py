# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150622_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agence',
            old_name='adresse',
            new_name='adresse_agence',
        ),
        migrations.RenameField(
            model_name='agence',
            old_name='distrib',
            new_name='distribue',
        ),
        migrations.RenameField(
            model_name='agence',
            old_name='nom',
            new_name='nom_agence',
        ),
    ]
