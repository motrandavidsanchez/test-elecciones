# Generated by Django 4.2.7 on 2024-06-10 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodirectory', '0002_alter_establishment_options_alter_locality_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='establishment',
        ),
    ]
