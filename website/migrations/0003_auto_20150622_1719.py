# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150622_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agence',
            name='adresse',
            field=models.CharField(max_length=100),
        ),
    ]
