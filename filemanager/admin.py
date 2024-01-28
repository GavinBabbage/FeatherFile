from django.contrib import admin

from . import models

class FilesAdmin(admin.ModelAdmin):
    list_display = ('file',)

admin.site.register(models.Files, FilesAdmin)
