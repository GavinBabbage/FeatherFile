# Generated by Django 4.1 on 2022-08-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0013_files_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='user',
        ),
        migrations.AddField(
            model_name='files',
            name='filedetails',
            field=models.CharField(default='These are the details of the file', max_length=200),
        ),
    ]
