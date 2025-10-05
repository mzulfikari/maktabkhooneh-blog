from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .views import Index



class TestUrl(SimpleTestCase):
    
    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class,Index)
