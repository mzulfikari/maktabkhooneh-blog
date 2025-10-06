from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from ..views import Index,PostDetail,Posts



class TestUrl(SimpleTestCase):
    
    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class,Index)
        
    def test_blog_post_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class,Posts)
        
    def test_blog_post_detail_url_resolve(self):
        url = reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,PostDetail)
