from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('phone','is_student',)