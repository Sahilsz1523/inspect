from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
send_mail('Test Subject', 'This is a test email.', 'sahilsn2005@gmail.com', ['recipient@gmail.com'])

