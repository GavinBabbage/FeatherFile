# Generated by Django 4.1 on 2022-09-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0029_remove_files_folder_alter_files_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='folder',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]
