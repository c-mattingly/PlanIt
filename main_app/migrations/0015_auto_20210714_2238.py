# Generated by Django 3.1.6 on 2021-07-14 22:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_merge_20210714_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='begin',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='proposal',
            name='finish',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, null=True, size=None),
        ),
    ]
