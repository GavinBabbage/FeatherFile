# Generated by Django 4.1 on 2022-09-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0019_files_folder_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=models.TextField(blank=True, max_length=20, null=True)),
        ),
        migrations.AlterField(
            model_name='files',
            name='folder',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]