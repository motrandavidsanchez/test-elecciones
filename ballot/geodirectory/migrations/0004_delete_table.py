# Generated by Django 4.2.7 on 2024-06-10 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodirectory', '0003_remove_table_establishment'),
        ('voting', '0006_remove_voter_table_voter_establishment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Table',
        ),
    ]