# Generated by Django 5.1.2 on 2024-12-23 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimagepost',
            old_name='title',
            new_name='description',
        ),
    ]
