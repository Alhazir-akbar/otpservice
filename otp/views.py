from django.shortcuts import render
import random
from datetime import datetime
from otp.models import Otpservice

def create_expired_unixtime(expired=None):              #Defenisi expired default none
    if expired == None:                                 #kalo expired none maka 
        expired = 5                                     #isi expired = 5
    curent_time = datetime.now()                        #waktu saat ini
    curent_unix_time = curent_time.timestamp()          #waktu saat ini convert menjadi nilai unix (di hitung dalam satuan detik dari tahun 1970)
    expired_time = curent_unix_time + (expired * 60)    #nilai unix 5*60
    return expired_time

def generate_random_otp():                              # Generate Method
    fixed_digits = 6                                    # Generate a random OTP with 6 digits.
    return random.randint(10 ** (fixed_digits - 1), (10 ** fixed_digits) - 1)   # Hitung Hitungan rumit untuk mendapatkan 6 angka acak

def create_otp(data):
    try:
        otp = generate_random_otp()                     #1. Try otp = method generate 
        expired_time = int(create_expired_unixtime())   #2. expired_time = hasil dari method create_expired_unixtime dengan return expired_time
        
        Otpservice(                                     #3. Models Otpservice
            phone_number = data['phone_number'],        #4. isi phone number
            otp_number = otp,                           #5. otp_number = otp = generate_random_otp = return random.randint
            expired_unixtime = expired_time             #6. expired_unixtime = expired_time = expired = 5 * 60
        ).save()                                        #7. Save
    except Exception as e:
        return False,str(e)
    return True, otp
    