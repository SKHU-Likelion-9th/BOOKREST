from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='coninggu@example.com',
            name='coninggu',
            password='testpassword12!@#',
        )
        self.assertEqual(user.email, 'coninggu@example.com')
        self.assertEqual(user.name, 'coninggu')
        self.assertFalse(user.is_admin)
        self.assertTrue(user.is_active)

    def test_crete_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            name='superuser',
            password='testpassword12!@#',
        )
        self.assertEqual(user.email, 'm1@gmail.com')
        self.assertEqual(user.name, 'kji')
        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_active)