from django import forms
from .models import Events, Gallery, Resources, Team
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

######################################################

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields =['event_name','organization', 'type', 'from_date', 'to_date', 'location','description','resource_persons','male_participants','female_participants','total_participants', 'photo', 'document']
        widgets = {
            'total_participants': forms.NumberInput(attrs={'readonly': 'readonly'})
        }


##############################################
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['activity', 'type', 'date', 'location', 'document']

#######################################################
class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ['type', 'name', 'date', 'description', 'document']

#################################################
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['first_name', 'last_name', 'contact_no', 'email_id', 'work_location', 'address', 'photo']