from django import forms 
from .models import Item, Outgoing, Incoming

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ['name', 'quantity', 'restock_alert']

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ['name', 'restock_alert']

class GiveItemForm(forms.ModelForm):
    class Meta:
        model = Outgoing
        fields = ['quantity_given']

class ReceiveItemForm(forms.ModelForm):
    class Meta:
        model = Incoming
        fields = ['quantity_received', 'vendor']