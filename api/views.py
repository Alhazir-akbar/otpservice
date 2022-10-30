from email import message
from http import server
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from api.serializers import CreateOTPSerializer, ValidateOTPSerializer
from otp.views import create_otp, validateOTP
from api.decorators import is_auth_user
from django.utils.decorators import method_decorator

# Create your views here.

class RestAPICreateOTP(APIView):
    @method_decorator(is_auth_user)
    def post(self, *args, **kwargs):
        try:
            data = JSONParser().parse(self.request)
            serializer = CreateOTPSerializer(data=data)
            if serializer.is_valid():
                is_otp, otp = create_otp(data)
                if is_otp == True:
                    return JsonResponse(data={
                        'message': 'success',
                        'status': '00',
                        'otp_number': otp
                    }, status=200)
                else:
                    return JsonResponse(data={
                        'message': 'Create OTP Failed',
                        'status': '-1'
                    }, status=400)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse(data={
                    'message': str(e),
                    'status': '-1'
                }, status=400)


class RestAPIValidatOTP(APIView):
    @method_decorator(is_auth_user)
    def post(self, *args, **kwargs):
        try:
            data = JSONParser().parse(self.request)
            serializer = ValidateOTPSerializer(data=data)
            if serializer.is_valid():
                is_validate_otp, message = validateOTP(data)
                if is_validate_otp == True:
                    return JsonResponse(data={
                        'message': message,
                        'status': '00'
                    }, status=200)
                else:
                    return JsonResponse(data={
                        'message': message,
                        'status': '-1'
                    }, status=400)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse(data={
                    'message': str(e),
                    'status': '-1'
                }, status=400)

