from django.test import TestCase
from otp.views import create_otp, generate_random_otp


# Create your tests here.
class CreateOtpTestCase(TestCase):
    sample_data = {
        'phone_number':'62878787123'
    }
    def test_create_otp_succes(self):
        status, otp = create_otp(self.sample_data)
        self.assertEqual(status, True)
        self.assertEqual(len(str(otp)), 6)
        
    def test_create_otp_failed(self):
        status, message = create_otp({})
        self.assertEqual(status, False)
        self.assertRaisesMessage(Exception, message)
        
    def test_generate_random_otp_succes(self):
        otp = generate_random_otp()
        self.assertEqual(len(str(otp)), 6)
        
        
