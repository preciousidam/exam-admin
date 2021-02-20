from mailer.views import VerifyEmail
from django.urls import path

urlpatterns = [
    path("verify/user/<int:pk>/", VerifyEmail.as_view(), name="Verify email with otp")
]
