from django.shortcuts import render, redirect

from doctor_app.forms import PrescriptionForm
from doctor_app.models import Prescription
from ehospital_app.forms import DoctorForm, AppointmentForm
from ehospital_app.models import Doctor, Appointment, Patient, MedicalHistory


# Create your views here.


def create_doctor(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')  # Redirect to a view that lists doctors, update this as necessary
    else:
        form = DoctorForm()
    return render(request, 'doctor_user/create_doctor_details.html', {'form': form, 'doctors': doctors})

def doctor_update_view(request,doctors_id):

    doctors = Doctor.objects.get(id=doctors_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctors)

        if form.is_valid():
            form.save()

            return redirect('doctors_list')
    else:
        form = DoctorForm(instance=doctors)

    return render(request, 'doctor_user/doctor_update.html', {'form': form, 'doctors': doctors })




def doctorslist(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    appointments = Appointment.objects.all()
    medical_history = MedicalHistory.objects.all()
    prescriptions = Prescription.objects.all()


    return render(request,'doctor_user/doctorslist.html',{'doctors':doctors,'patients': patients,'appointments': appointments, 'medical_history': medical_history,'prescriptions': prescriptions })


def userdetails_doctor(request,doctors_id):
    doctors = Doctor.objects.get(id=doctors_id)

    return render(request,'doctor_user/doctordetails.html',{'doctors':doctors})


def doctor_deleteView(request,doctors_id):

    doctors = Doctor.objects.get(id=doctors_id)

    if request.method=='POST':
        doctors.delete()

        return redirect('doctors_list')



    return render(request,'doctor_user/doctor_deleteview.html',{'doctors':doctors})




def update_appointment(request, appointment_id):
    appointments = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointments)

        if form.is_valid():
            form.save()

            return redirect('doctors_list')
    else:
        form = AppointmentForm(instance=appointments)

    return render(request, 'update_appointment.html', {'form': form, 'appointments': appointments})

def appoinment_details_doctor(request,appointment_id):
    appointments = Appointment.objects.get(id=appointment_id)

    return render(request,'doctor_user/doctor_appoinment_details.html',{'appointments':appointments})

def create_prescription(request):
    prescriptions = Prescription.objects.all()
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor_user/create_prescription.html', {'form': form, 'prescriptions': prescriptions})

def prescription_details(request,prescriptions_id):
    prescriptions = Prescription.objects.get(id=prescriptions_id)

    return render(request,'doctor_user/prescription_details.html',{'prescriptions':prescriptions})