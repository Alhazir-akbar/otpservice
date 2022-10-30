from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.

class RestAPICreateOTPTestCase(APITestCase):
    def test_create_otp_succes(self):
        self.assertEquals("","")