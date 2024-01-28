import urllib
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
from urllib import request

from django.db import models
from django.conf import settings
import os
# from .models import Folder
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Models to handle file uploads

class Files(models.Model):
    
    filename = models.CharField(max_length=20, null=False, blank=True)
    file = models.FileField(upload_to='uploadedFiles/')
    uploadedAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", default=1)

    # def save(self):
    #     if not self.filename:
    #         self.filename = self.file.name
    #     return super().save()


    def __str__(self):
        return self.filename

