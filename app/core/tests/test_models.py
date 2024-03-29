from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'ablanyaalec@gmail.com'
        password = 'OPPIO)L'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'ablanyalex@gmAil.com'
        user = get_user_model().objects.create_user(email, 'Test123')

        self.assertEqual(user.email, email.lower())

    
    def test_new_user_invaild_email(self):
        """Test creating user with no email raises errro"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user =  get_user_model().objects.create_superuser(
            'ablanyaalex@gmail.com',
            'test123'
        )
        