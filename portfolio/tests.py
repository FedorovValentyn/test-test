from django.test import TestCase, Client
from django.urls import reverse
from .models import Project

class PortfolioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення тестових даних
        Project.objects.create(
            title='Test Project',
            description='Test Description',
            url='http://example.com'
        )

    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_projects_view(self):
        client = Client()
        response = client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/projects.html')

    def test_contact_view(self):
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')