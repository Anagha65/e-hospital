from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, MedicalHistory, Billing, Doctor, HealthEducationResource
from .forms import PatientRegistrationForm, AppointmentForm, MedicalHistoryForm, DoctorForm, BillingForm, \
    HealthEducationResourceForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def patient_registration(request):
    patients = Patient.objects.all()
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register.html', {'form': form, 'patients': patients})

def patient_dashboard(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    medical_history = MedicalHistory.objects.all()
    billings = Billing.objects.all()
    resources = HealthEducationResource.objects.all()
    return render(request, 'patient_dashboard.html', {
        'patients': patients,
        'appointments': appointments,
        'medical_history': medical_history,
        'billings': billings,
        'doctors': doctors,
        'resources': resources,
    })


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})


def update_appointment(request,appointment_id):

    appointments = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointments)

        if form.is_valid():
            form.save()

            return redirect('patient_dashboard')
    else:
        form = AppointmentForm(instance=appointments)

    return render(request, 'update_appointment.html', {'form': form, 'appointments': appointments })







def medical_history_details(request, history_id):
    medical_history = MedicalHistory.objects.get(id=history_id)
    return render(request, 'medical_history_details.html', {'medical_history': medical_history})


def create_medical_history(request):
    medical_history = MedicalHistory.objects.all()
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = MedicalHistoryForm()
    return render(request, 'medical_history.html', {'form': form, 'medical_history': medical_history })


def update_medical_history(request,history_id):
    medical_history = MedicalHistory.objects.get(id=history_id)

    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, request.FILES, instance=medical_history)

        if form.is_valid():
            form.save()

            return redirect('patient_dashboard')
    else:
        form = MedicalHistoryForm(instance=medical_history)

    return render(request, 'update_medical_history.html', {'form': form, 'medical_history': medical_history})


def create_doctor(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')  # Redirect to a view that lists doctors, update this as necessary
    else:
        form = DoctorForm()
    return render(request, 'create_doctor.html', {'form': form, 'doctors': doctors})


def add_billing(request):
    billings = Billing.objects.all()
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')  # Redirect to a view that lists billing records
    else:
        form = BillingForm()
    return render(request, 'add_billing.html', {'form': form, 'billings': billings})

def update_billing(request, billing_id):
    billings = Billing.objects.get(id=billing_id)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=billings)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')  # Redirect to a view that lists billing records
    else:
        form = BillingForm(instance=billings)
    return render(request, 'update_billing.html', {'form': form, 'billings': billings})




def add_health_education_resource(request):
    resources = HealthEducationResource.objects.all()
    if request.method == 'POST':
        form = HealthEducationResourceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = HealthEducationResourceForm()
    return render(request, 'add_health_education_resource.html', {'form': form, 'resources': resources })

def update_health_educational_resource(request,resource_id):
    resources = HealthEducationResource.objects.get(id=resource_id)
    if request.method == 'POST':
        form = HealthEducationResourceForm(request.POST,request.FILES, instance=resources)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')  # Redirect to a view that lists billing records
    else:
        form = HealthEducationResourceForm(instance=resources)
    return render(request, 'update_resource.html', {'form': form, 'resources': resources})

def resource_details(request, resource_id):
    resources = HealthEducationResource.objects.get(id=resource_id)
    return render(request, 'resource_details.html', {'resources': resources})

