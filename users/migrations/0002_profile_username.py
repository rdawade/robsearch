# Generated by Django 3.2.5 on 2021-07-25 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.EmailField(blank=True, max_length=500, null=True),
        ),
    ]
