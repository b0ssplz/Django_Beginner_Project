from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="test_user", 
                                                    email="test@mail.com",
                                                    password="test123")
        


    def test_user_creation(self):
        user = get_user_model().objects.get(id=1)
        
        self.assertEqual(self.user.username, user.username)