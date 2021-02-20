from django.core.mail import BadHeaderError, send_mail
from smtplib import SMTPException
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from pyotp import HOTP
from datetime import datetime
import base64

from harrp.models import User
from core.settings import SECRET_KEY
from harrp.serializers import UserSerializer

class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + SECRET_KEY


class VerifyEmail(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, pk):
        user = User.objects.get(pk=pk)
        user.verify_count += 1
        user.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(user.phone).encode())
        OTP = HOTP(key)

        try:
            res = send_mail(
                "Email verification",
                f'Dear {user.first_name}\n\n Please use this six digit code {OTP.at(user.verify_count)} to verify your account.\n Valid for 30sec.\n\n Thank you.',
                'test@prestone.com.ng',
                [user.email],
                fail_silently=False,
            )
            return Response({'message': f'Verification mail Sent to {user.email}'}, status.HTTP_200_OK)
        except BadHeaderError as e:
            return Response({'message': 'Invalid header found.'}, status.HTTP_400_BAD_REQUEST)
        except SMTPException as e:
            print(e)
            return Response({'message': 'Something Happened.'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    @staticmethod
    def post(request, pk):
        user = User.objects.get(pk=pk)
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(user.phone).encode())
        OTP = HOTP(key)

        otp_data = request.data['otp']
       
        
        if OTP.verify(otp_data, user.verify_count):
            user.verified = True
            user.save()
            return Response({'message': f'{user.email} verified', 'user': UserSerializer(user, context={'request': request}).data}, status.HTTP_200_OK)

        return Response({'message': "OTP is wrong or has expired"}, status.HTTP_400_BAD_REQUEST)
