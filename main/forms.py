from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "C1", "C2", "name", "image", "sum", "stock", "using",
            "location", "user", "number", "bo_date", "re_date", "back_or_not"
        ]