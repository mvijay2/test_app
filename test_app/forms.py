from django import forms
from .models import Events
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('email',)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Try logging in instead.")
        return email


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model=CustomUser
        fields=('email',)

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date', 'event_time', 'event_location', 'event_description']
