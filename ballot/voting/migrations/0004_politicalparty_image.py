# Generated by Django 4.2.7 on 2024-06-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_politicalparty_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalparty',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]