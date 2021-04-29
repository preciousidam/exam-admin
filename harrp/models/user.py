from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import date
import time

from harrp.constants import LEVEL, STATE, COUNTRY, GENDER



class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone',]
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone = models.CharField(_("Phone"), max_length=15)
    verify_count = models.IntegerField(_("Count"), default=0, blank=False)
    verified = models.BooleanField(_("Verified"), default=False, help_text="Phone number verified?")
    is_student = models.BooleanField(_("Student?"), help_text="Select is student user", null=True, default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
	

class StudentProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(_("Address"), max_length=255)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), max_length=255, choices=STATE)
    country = models.CharField(_("Country"), max_length=50, choices=COUNTRY)
    dob = models.DateField(_("Date Of Birth"))
    gender = models.CharField(_("Gender"), max_length=50, choices=GENDER)
    level = models.CharField(_("Level"), max_length=50, choices=LEVEL)
    id_number = models.CharField(_("Identification"), max_length=50, null=True, blank=True, help_text="Matric no / Exam No/ Registration No")
    guard_one_email = models.EmailField(_("Email"), max_length=254)
    guard_two_email = models.EmailField(_("Email"), max_length=254, null=True, blank=True)
    guard_one_phone = models.CharField(_("Phone"), max_length=15)
    guard_two_phone = models.CharField(_("Phone"), max_length=15, null=True, blank=True)

    class Meta:
        ordering = ['user__first_name', 'user__last_name', 'level']

    def __str__(self):
        return f'{self.user} Profile'

    def get_user(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse("student_profile", kwargs={"id": self.id})
    



