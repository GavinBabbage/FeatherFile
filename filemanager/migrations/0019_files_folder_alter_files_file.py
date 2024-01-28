# Generated by Django 4.1 on 2022-09-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0018_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='folder',
            field=models.TextField(default='media/', max_length=20),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=models.TextField(default='media/', max_length=20)),
        ),
    ]
