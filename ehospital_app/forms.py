from django import forms
from django.contrib.auth.models import User
from .models import Patient, Appointment, MedicalHistory, Doctor, Billing, HealthEducationResource


class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }




class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields ='__all__'

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'medications': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'treatment_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'record_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name', 'specialization', 'phone_number']
        widgets = {
            'doc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'amount', 'billing_date', 'status']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'billing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class HealthEducationResourceForm(forms.ModelForm):
    class Meta:
        model = HealthEducationResource
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),

            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

