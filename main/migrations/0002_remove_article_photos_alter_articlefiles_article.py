# Generated by Django 5.0.6 on 2024-11-18 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photos',
        ),
        migrations.AlterField(
            model_name='articlefiles',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.article'),
        ),
    ]