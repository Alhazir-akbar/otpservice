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
        expired_time = int(create_expired_unixtime())
        
        Otpservice(
            phone_number = data['phone_number'],
            otp_number = otp,
            expired_unixtime = expired_time
        ).save()
    except Exception as e:
        return False,str(e)
    return True, otp
    
def checkExistOtp(data):
    try:
        checkOTP = Otpservice.objects.filter(phone_number=data['phone_number'], otp_number=data['otp_number'])
        if len(checkOTP) > 0:
            return True, checkOTP[0], ""
        return False, "", "OTP Number not found"
    except Exception as e:
        return False, "", str(e)
    
def checkOTPExpired(expired_unixtime):
    curent_time = datetime.now()
    curent_unix_time = curent_time.timestamp()
    if int(curent_unix_time) < int(expired_unixtime):
        return True, "OTP valid"
    else:
        return False, "OTP Expired"
    
def validateOTP(data):
    try:
        is_optexist, otp, messageIsExist = checkExistOtp(data)
        if is_optexist == True:
            if otp.validate == True:
                return False, "OTP already used"
            is_expired, messageIsExpired = checkOTPExpired(otp.expired_unixtime)
            if is_expired == True:
                otp.validate = True
                otp.save()
                return True, "success"
            else:
                return is_expired, messageIsExpired
        else:
            return is_optexist, messageIsExist
    except Exception as e:
        return False, str(e)
    