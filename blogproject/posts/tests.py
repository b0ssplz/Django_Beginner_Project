from urllib import response
from django.test import TestCase
from .models import Post

# Create your tests here.


class PostTestCase(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title="Test_title", 
                                        author="Test_author", 
                                        content="Test_content")
        
        
    
    
    def test_home_page(self):
        response = self.client.get('/index/')
        
        self.assertEqual(response.status_code,200)       
        self.assertTemplateUsed(response,'index.html')
        self.assertContains(response,"List of mangas")
        
    
    def test_post_creation(self):
        post_to_test = Post.objects.get(id=1)
        
        post_title = f"{post_to_test.title}"
        
        self.assertEqual(self.post.title, post_to_test.title)
        self.assertEqual(self.post.author, "Test_author")
