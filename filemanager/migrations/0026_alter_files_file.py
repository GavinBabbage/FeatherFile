# Generated by Django 4.1 on 2022-09-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0025_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=models.TextField(blank=True, max_length=20)),
        ),
    ]
