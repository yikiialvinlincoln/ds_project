# Generated by Django 5.0.6 on 2024-05-21 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='doll_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daycare.doll_type'),
        ),
    ]
