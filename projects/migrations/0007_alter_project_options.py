# Generated by Django 3.2.5 on 2021-08-03 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
