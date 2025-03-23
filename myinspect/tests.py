from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
send_mail('Test Subject', 'This is a test email.', 'sahilsn2005@gmail.com', ['recipient@gmail.com'])

from django.test import TestCase
from django.contrib.auth.models import User
from myinspect.models import Visitor  # Make sure this is your correct app name

class VisitorModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="testuser", password="testpassword")

    def test_create_visitor(self):
        visitor = Visitor.objects.create(
            user=self.user,  # Add this line to assign the user
            name="John Doe",
            phone="1234567890",
            address="123 Street",
            email="john@example.com",
            description="Visiting for business"
        )
        self.assertEqual(visitor.name, "John Doe")
from django.test import TestCase
from myinspect.forms import VisitorForm

class VisitorFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'Alice', 'phone': '9876543210', 'email': 'alice@example.com', 'address': '123 St', 'description': 'Meeting'}
        form = VisitorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'name': '', 'phone': '98765', 'email': 'wrongemail', 'address': '', 'description': ''}
        form = VisitorForm(data=form_data)
        self.assertFalse(form.is_valid())
from django.test import TestCase
from django.urls import reverse

class VisitorViewTest(TestCase):
    def test_visitor_list_view(self):
        response = self.client.get(reverse('visitor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visitor_list.html')
from rest_framework.test import APITestCase
from django.urls import reverse

class VisitorAPITest(APITestCase):
    def test_get_visitors(self):
        url = reverse('visitor_api_list')  # Adjust with your actual API URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTest(TestCase):
    def test_login_required_for_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login
