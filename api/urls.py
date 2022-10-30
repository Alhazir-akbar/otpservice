
from unicodedata import name
from django.urls import path
from api.views import RestAPICreateOTP, RestAPIValidatOTP

urlpatterns = [
    path('v1/otp/create/', RestAPICreateOTP.as_view(), name='api_create_otp'),
    path('v1/otp/validate-otp/', RestAPIValidatOTP.as_view(), name='api_validate_otp'),
]
