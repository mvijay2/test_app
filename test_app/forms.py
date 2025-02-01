from django import forms
from .models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date', 'event_time', 'event_location', 'event_description']
