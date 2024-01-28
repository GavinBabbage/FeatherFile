


from unittest import TestCase
from django.test import Client
from django.urls import resolve, reverse
from filemanager.models import Files

class TestViews(TestCase):
    