from django.forms import ModelForm
from main.models import NelayanEntry

class NelayanEntryForm(ModelForm):
    class Meta:
        model = NelayanEntry
        fields = ["name", "price", "description"]