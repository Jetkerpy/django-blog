from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from django.forms import ValidationError
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["username", "email", "age"]

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise ValidationError("Your age is not included, sorry!")
        
        return age


class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = "__all__"