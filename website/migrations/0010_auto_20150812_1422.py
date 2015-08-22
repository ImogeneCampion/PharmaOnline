# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150812_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='compagnie',
            field=models.CharField(max_length=45, default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Compagnie',
        ),
    ]
