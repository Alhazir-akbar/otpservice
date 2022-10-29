from django.test import TestCase
from otp.views import create_otp, generate_random_otp, validateOTP


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
        
        
class ValidateOTPTestCase(TestCase):
    payload_create_otp = {
        'phone_number':'62878787123'
    }
    
    def test_validate_otp_succes(self):
        status, otp = create_otp(self.payload_create_otp)
        payload_validate_otp = {
            'phone_number':'62878787123',
            'otp_number': otp
        }
        status, message = validateOTP(payload_validate_otp)
        self.assertEqual(status, True)
        
    def test_validate_otp_failed(self):
        payload_validate_otp = {
            'phone_number':'62878787123',
            'otp_number': '123456'
        }
        status, message = validateOTP(payload_validate_otp)
        self.assertEqual(status, False)
        
        
