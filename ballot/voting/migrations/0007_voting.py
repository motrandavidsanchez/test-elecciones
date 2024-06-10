# Generated by Django 4.2.7 on 2024-06-10 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geodirectory', '0004_delete_table'),
        ('voting', '0006_remove_voter_table_voter_establishment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting', models.BooleanField(default=False, verbose_name='Votación')),
                ('establishment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geodirectory.establishment', verbose_name='Establecimiento')),
            ],
            options={
                'verbose_name': 'Votación',
                'verbose_name_plural': 'Votaciones',
            },
        ),
    ]
