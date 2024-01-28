from django.shortcuts import render, redirect
import os
import zipfile
from io import BytesIO

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView
from .models import Files
from .forms import FilesForm
from django.http import StreamingHttpResponse, Http404
import directory.views
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import shutil
from pathlib import Path



# method to upload single and multiple files
def upload(request):
    if request.method == 'POST':
        filein = request.FILES.getlist("file")
        for f in filein:
            new_file = Files(
                filename=f,
                file=f
            )
            new_file.user = request.user
            new_file.save()
            
            # fileName = str(new_file.filename)
            # print("file name:",fileName)
            # move(request, fileName)


        messages.success(request, "Upload successful.", extra_tags='alert')
        return redirect(request.META['HTTP_REFERER'])
        # url = reverse('uploadfile')
        # return redirect(url)
        
    else:
        form = FilesForm()
    return render(request, 'filemanager/files_form.html', {'form': form})



# method to create a new folder
def makedir(request): 

    if request.method == 'POST':
        name = request.POST['folder_name']

        try:
            path = os.path.join(settings.MEDIA_ROOT, name)
            os.mkdir(path)
            messages.success(request, str(name) + " Directory has been created.")
            # print("The directory ", name, "has been created.")
        
        # message for when the directory already exists
        except FileExistsError:
            # print('Directory already exists')
            messages.error(request, str(name) + " Directory already exists.")
    return redirect(request.META['HTTP_REFERER'])
    


# method to rename directories
def rename(request, oldname):  
    print("old name: ", oldname)
    if request.method == 'POST':
        try:
            # name =oldname #request.POST['folder_name']
            name = oldname.split("\\")[-1]
            newname = request.POST['newfolder_name']
            # path = os.path.join(settings.MEDIA_ROOT, name)
        
            # pathString = str(oldname)
            oldPath = os.path.join(settings.DIRECTORY_DIRECTORY,Path(oldname))
            # print("old name path: ", oldPath)
            oldPathString = str(oldPath)
            newPathString = oldPathString.replace(name, newname)
            # print("new path string: ", newPathString)
            newPath = Path(newPathString)

            os.rename(oldPath, newPath)
            messages.success(request, str(name) + " has been renamed " + str(newname) +".")
        
        # mismatch error
        except IsADirectoryError:
            # print("Source is a file but destination is a directory.")
            messages.error(request, "Source is a file but destination is a directory.", extra_tags='alert')

        
        # but destination is a file
        except FileExistsError:
            # print('Directory already exists')
            messages.error(request, "Directory already exists.", extra_tags='alert')

        # For permission related errors
        except PermissionError:
            # print("Operation not permitted.")
            messages.error(request, "Operation not permitted.", extra_tags='alert')
        # return HttpResponseRedirect('/fileman/dir/')
    return redirect(request.META['HTTP_REFERER'])


# method to move directories
def move(request, source):
    destination = request.POST['newfolder_name']
    if request.method == 'POST':
        try:
            
                path = os.path.join(settings.DIRECTORY_DIRECTORY, source)
                # print("source path: ", source)
                # print("path: ", path)

                # if the item being moved is a folder
                if os.path.isdir(path):
                    for destpath in Path(settings.MEDIA_ROOT).rglob(destination):
                        # print("source: ", path)

                        # print("destimation: ", destpath)
    
                    # destination = destinationpathstring
                        shutil.move(path, destpath)
                        messages.success(request, str(source) + " has been moved to " + str(destination) + ".")
                    # print("source path: ", sourcepath, "  destination path: ", destinationpath , "  dest path: ", dest)
                        break
                # break
                else:
                    # if the thing 
                    for destpath in Path(settings.MEDIA_ROOT).rglob(destination):
                        name = source.split("\\")[-1]
                        dest_path = os.path.join(destpath,name)
                        shutil.move(path, dest_path)
                        break

        except FileNotFoundError:
            # print('Either one of the directories does not exist.')
            messages.error(request, "Either one of the directories does not exist.", extra_tags='alert')
        # reloads the same page 
        return redirect(request.META['HTTP_REFERER'])





# method to delete folders and files

def delete(request, name):
    if request.method == 'POST':
        try:
            path = os.path.join(settings.DIRECTORY_DIRECTORY,name)
            # differentiate between folder and file
            if os.path.isfile(path):
                os.remove(path)
                messages.success(request, str(name) + " has been deleted.")
            else:
                shutil.rmtree(path)
                messages.success(request, str(name) + " has been deleted.")

        except FileNotFoundError:
            # print('File or directory does not exist')
            messages.error(request, "File or directory does not exist.", extra_tags='alert')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#method to batch download and download individual files, downloads files inside folders

def batch_download(request):
    # list of checked files from the form
    targets = request.POST["targets"]
    targets = targets.split(",")
    file_list = []
    print(targets)
    for filepath in targets:
        path = os.path.join(settings.DIRECTORY_DIRECTORY, filepath)
        # walk through the specified folder to download all the files inside the folder
        if os.path.isdir(path):
            for root, directories, files in os.walk(path):
                for filename in files:
                # Create the full filepath by using os module.
                    filePath = os.path.join(path, filename)
                    file_list.append(filePath)
        
        else:
            #if individual files are selected
            file_list.append(path)
       
    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(byte_data, "w")

    # write all the file paths to the zip file
    for file in file_list:
        filename = os.path.basename(file)
        zip_file.write(file, filename)

    zip_file.close()
    # download the single file if one was created
    if len(file_list)==1:
        
        response = StreamingHttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(Path(file_list[0]))
        file_obj = open(Path(file_list[0]), 'rb')
        response.streaming_content = directory.views.read_file_chunkwise(file_obj)
        return response
    
    # if the is a batch, download the zipped folder
    response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=files.zip'

    return response



    