from rest_framework import serializers

class CreateOTPSerializer(serializers.Serializer):
   phone_number = serializers.CharField(max_length=50)
   
class ValidateOTPSerializer(serializers.Serializer):
   phone_number = serializers.CharField(max_length=50)
   otp_number = serializers.CharField(max_length=50)