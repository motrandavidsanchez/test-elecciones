# Generated by Django 4.2.7 on 2024-06-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_voter_table_alter_politicalparty_party_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalparty',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Votos'),
        ),
    ]
