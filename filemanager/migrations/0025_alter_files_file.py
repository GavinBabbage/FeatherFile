# Generated by Django 4.1 on 2022-09-15 15:40

from django.db import migrations, models
import filemanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0024_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=filemanager.models),
        ),
    ]
