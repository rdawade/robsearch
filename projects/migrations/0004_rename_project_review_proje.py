# Generated by Django 3.2.5 on 2021-07-18 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_review_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='project',
            new_name='proje',
        ),
    ]
