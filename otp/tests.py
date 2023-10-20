from django.test import TestCase
from otp.views import create_otp, generate_random_otp

# Import modul yang dibutuhkan dan model/fungsi yang akan diuji.

class CreateOtpTestCase(TestCase):
    sample_data = {
        'phone_number': '62878787123'
    }

    # Membuat kelas pengujian (test case) yang merupakan turunan dari TestCase.

    def test_create_otp_succes(self):
        # Membuat metode pengujian untuk kasus berhasil membuat OTP.
        status, otp = create_otp(self.sample_data)  # Memanggil fungsi create_otp dengan data sampel.
        self.assertEqual(status, True)              # Memeriksa apakah status kembalian adalah True.
        self.assertEqual(len(str(otp)), 6)          # Memeriksa apakah panjang OTP adalah 6 digit.

    def test_create_otp_failed(self):
        # Membuat metode pengujian untuk kasus gagal membuat OTP.
        status, message = create_otp({})                # Memanggil fungsi create_otp dengan data kosong.
        self.assertEqual(status, False)                 # Memeriksa apakah status kembalian adalah False.
        self.assertRaisesMessage(Exception, message)    # Memeriksa apakah pengecualian Exception terjadi dengan pesan tertentu.

    def test_generate_random_otp_succes(self):
        # Membuat metode pengujian untuk kasus berhasil menghasilkan OTP acak.
        otp = generate_random_otp()         # Memanggil fungsi generate_random_otp.
        self.assertEqual(len(str(otp)), 6)  # Memeriksa apakah panjang OTP adalah 6 digit.

# Ini adalah tes pengujian Django yang melakukan pengujian berdasarkan metode yang telah didefinisikan.
