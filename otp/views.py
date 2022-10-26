from django.shortcuts import render
import random
from datetime import datetime
from otp.models import Otpservice

def create_expired_unixtime(expired=None):
    if expired == None:
        expired = 5
    curent_time = datetime.now()
    curent_unix_time = curent_time.timestamp()
    expired_time = curent_unix_time + (expired * 60)
    return expired_time

def generate_random_otp():
    fixed_digits = 6
    return random.randrange(111111, 999999, fixed_digits)


def create_otp(data):
    try:
        otp = generate_random_otp()
        expired_time = int(create_expired_unixtime)
        
        Otpservice(
            phone_number = data['phone_number'],
            otp_number = otp,
            expired_unixtime = expired_time
        ).save()
    except Exception as e:
        return False,""
    return True, otp
    