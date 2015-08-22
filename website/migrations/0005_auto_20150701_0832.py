# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150630_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agence',
            old_name='adresse_agence',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='agence',
            old_name='nom_agence',
            new_name='nom',
        ),
    ]
