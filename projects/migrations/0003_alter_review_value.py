# Generated by Django 3.2.5 on 2021-07-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210718_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'up vote'), ('down', 'down vote')], max_length=200),
        ),
    ]
