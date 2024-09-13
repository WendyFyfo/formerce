from django.forms import ModelForm
from main.models import MoodEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["Name", "Price", "Description"]