from django.test import SimpleTestCase
from django.urls import resolve, reverse
from filemanager.views import upload, makedir, move, rename, batch_download, delete

class TestUrls(SimpleTestCase):

    def test_batch_download_url_is_resolves(self):
        url = reverse('batch_download')
        self.assertEquals(resolve(url).func, batch_download)
    
    def test_createFolder_url_is_resolves(self):
        url = reverse('createFolder')
        self.assertEquals(resolve(url).func, makedir)

    def test_uploads_url_is_resolves(self):
        url = reverse('uploadfile')
        self.assertEquals(resolve(url).func, upload)

    def test_move_url_is_resolves(self):
        url = reverse('move', args=['basename'])
        self.assertEquals(resolve(url).func, move)

    def test_delete_url_is_resolves(self):
        url = reverse('rename', args=['basename'])
        self.assertEquals(resolve(url).func, rename)

    def test_move_url_is_resolves(self):
        url = reverse('delete', args=['basename'])
        self.assertEquals(resolve(url).func, delete)
    