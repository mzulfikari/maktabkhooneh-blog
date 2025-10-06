from django.test import TestCase,SimpleTestCase
from..models import Category,Post
from accounts.models import User,Profile
from datetime import datetime

class TestPostModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com",password="a@1234567")
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = "test-first_name",
            last_name = "test_last_name",
            description = "test_description",
            nationality = "test_nationality",
            profession = "test_profession"
        )
        
    def test_create_post_with_valid_data(self):
        
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title,"test")