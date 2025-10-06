from django.test import TestCase,Client
from django.urls import reverse
from..models import Category,Post
from accounts.models import User,Profile
from datetime import datetime


class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create_user(email="test@test.com",password="a@1234567")
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = "test-first_name",
            last_name = "test_last_name",
            description = "test_description",
            nationality = "test_nationality",
            profession = "test_profession"
        )
        
        self.post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        
    def test_blog_index_url_successful_response(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,template_name="blog/index.html")
        
        
    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail',kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        
        
    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail',kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)