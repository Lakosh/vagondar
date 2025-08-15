from django import forms
from .models import Wagon, TrainEvent, Destination, TariffHistory


class AddWagonForm(forms.ModelForm):
    class Meta:
        model = Wagon
        fields = ["wagon_number", "destination", "notes"]


class AddEventForm(forms.ModelForm):
    class Meta:
        model = TrainEvent
        fields = ["operation_type", "event_date", "event_time", "tariff", "notes"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "event_time": forms.DateInput(attrs={"type": "time"}, format="%H:%M")
        }


class AddDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ["name", "distance_km"]


class AddTariffForm(forms.ModelForm):
    class Meta:
        model = TariffHistory
        fields = ["start_date", "tariff"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"})
        }


class AddWagonGenForm(forms.ModelForm):  # для создание вагонов с events
    class Meta:
        model = Wagon
        fields = ["wagon_number", "event", "destination", "notes"]

