from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from harrp import models

# Register your models here.
#from .models import InsuredProfile, Identification, OfficerProfile, InsuredOfficer, User
from harrp.models import User, StudentProfile, School
from harrp.forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','phone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_student',
                                       'verified', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone'),
        }),
    )

    list_display = ['email','first_name', 'last_name', 'phone', 'is_staff', 'is_student', 'verified']
    ordering = ['email', 'first_name', 'username', 'last_name', 'is_student', 'verified']
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(User, CustomUserAdmin)

class AttendingInline(admin.TabularInline):
    model = School.students.through
    verbose_name=_("School")
    verbose_name_plural=_("Schools Attended")
    extra=1

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('user',)}),
        (_('Personal Info'), {'fields': ('dob', 'gender','level', 'id_number')}),
        (_('Address'), {'fields': ('address', 'city', 'state', 'country',)}),
        (_('Guardian One'), {'fields': ('guard_one_email', 'guard_one_phone')}),
        (_('Guardian Two'), {'fields': ('guard_two_email', 'guard_two_phone')}),
    )

    list_display = ['get_user','dob', 'gender', 'address', 'id_number', 'level',]
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'id_number', 'id_number')
    inlines = [AttendingInline]
    exclude=('students',)