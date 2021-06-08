from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from subscription.serializers import PlanSerializer, SubscriptionSerializer
from harrp.models import User
from subscription.models import Plan, Subscription
from core.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from ..flutterwave import FlutterWave
from ..validators import validatePaymentDetails

# Create your views here.

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or  self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_permissions(self):
        permission_classes = [IsLoggedInUserOrAdmin]
        
        return [permission() for permission in permission_classes]


@api_view(['POST'])
@permission_classes((AllowAny,))
def pay_with_rave(request):

    error = validatePaymentDetails(request.data)
    
    if error.get('status') != 'ok':
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        rave = FlutterWave(cardno=request.data['cardno'], cvv=request.data['cvv'], 
                            expirymonth=request.data['expirymonth'], expiryyear=request.data['expiryyear'],
                            pin=request.data['pin'], amount=request.data['amount'], user=user)

        res = rave.pay_via_card()

        if res['status'] != 'success':
            return Response({'msg': res['data']['message'], 
                            'code': res['data']['code'], 'status': res['status']}, status=status.HTTP_400_BAD_REQUEST)
                            

        elif res['status'] == 'success' and res['data']['chargeResponseCode'] == "02":
            return Response({'msg': res['data']['chargeResponseMessage'], 
                            'code': res['data']['chargeResponseCode'], 
                            'status': res['status'],
                            'ref': res['data']['flwRef']},
                            status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return Response({"status": "failed", "msg": "something happened server cannot handle this request at the moment try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes((AllowAny,))
def validate_with_OTP_rave(request):

    otp = request.data['otp']
    policy = request.data['policy_number']
    amount = request.data['amount']
    ref = request.data['ref']
    plan = request.data['plan']
    user = request.data['user']
    
    if not otp or not ref or not policy or not amount or not plan or not user:
        return Response({"status": "failed", "msg": "Bad request some fields are missing from request body"}, 
                        status=status.HTTP_400_BAD_REQUEST)
    try:
       
        rave = FlutterWave()

        res = rave.validatePayment(ref=ref, otp=otp)

        if res['status'] != 'success':
            return Response({'msg': res['message'], 'status': res['status']}, status=status.HTTP_400_BAD_REQUEST)

                       
        if res['status'] == 'success' and res['data']['data']['responsecode'] == "00":

            verify = rave.verifyPayment(res['data']['tx']['txRef'],amount)
            
            if verify == False:
                return Response({"status": "failed", "msg": "Provide amount doesn't match charged amount"}, status=status.HTTP_400_BAD_REQUEST)

            payment = Subscription(user=user, pay_ref=ref, plan=plan)
            payment.save()

            return Response({'msg': res['data']['data']['responsemessage'], 
                            'code': res['data']['data']['responsecode'], 'status': res['status']}, 
                            status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({"status": "failed", "msg": "something happened server cannot handle this request at the moment try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
