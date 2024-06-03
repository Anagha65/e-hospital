from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['fac_name', 'location', 'department', 'resources']
        widgets = {
            'fac_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'resources': forms.Textarea(attrs={'class': 'form-control'}),
        }