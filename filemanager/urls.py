import re
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views 
from django.conf.urls.static import static
from django.conf.urls import include


urlpatterns = [
    
    path('filemanager/list/rename/<oldname>', views.rename, name= 'rename'),
    # path('filemanager/list/rename/<oldname>', FileOperations.FileOperations.rename, name= 'rename'),
    path('filemanager/list/move/<source>', views.move, name= 'move'),
    path('filemanager/<name>', views.delete, name= 'delete'),
    path('filemanager/newupload/', views.upload, name='uploadfile'),
    path('filemanager/NewFolder/', views.makedir, name='createFolder'),
    path('fileman/download/', views.batch_download, name='batch_download'),
    path('fileman/dir/', include('directory.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
