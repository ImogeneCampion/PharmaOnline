# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150701_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='categorie',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
