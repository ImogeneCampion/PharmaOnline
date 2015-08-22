# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_medicament_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='compagnie',
            field=models.CharField(max_length=45),
        ),
    ]
