from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


user = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email'