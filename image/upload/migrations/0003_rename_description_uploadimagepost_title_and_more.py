# Generated by Django 5.1.2 on 2024-12-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_rename_title_uploadimagepost_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimagepost',
            old_name='description',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='uploadimagepost',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
