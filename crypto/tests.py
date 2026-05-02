from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status_code(self):
        """Test that the home page returns a 200 status code."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        """Test that the home page uses the correct template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_contains_welcome_text(self):
        """Test that the home page contains the welcome text."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Welcome To CryptoWorld")

    def test_home_page_context_data(self):
        """Test that the home page context contains the expected data keys."""
        response = self.client.get(reverse('home'))
        self.assertIn('api', response.context)
        self.assertIn('price', response.context)
