from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'pay/rave/validate/', validate_with_OTP_rave),
    url(r'pay/rave/', pay_with_rave),
]