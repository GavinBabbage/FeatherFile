from cProfile import label
from django.core.exceptions import ValidationError
from django import forms
from django.http import request
from .models import Files

# files form to handle file uploads
class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file', )
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control my-5', 'multiple': True}),
        }
        labels = {
            'file': "Choose a file to upload",
        }
