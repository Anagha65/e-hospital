from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from admin_app.forms import FacilityForm
from admin_app.models import Facility
from ehospital_app.forms import AppointmentForm
from ehospital_app.models import Appointment, Patient


# Create your views here.



def userlist(request):
    facilities = Facility.objects.all()
    appointments = Appointment.objects.all()
    patients = Patient.objects.all()
    users = User.objects.all()

    return render(request, 'user_admin/userlist.html', {
        'facilities': facilities,
        'appointments': appointments,
        'patients': patients,
        'users': users,
    })
def user_book_appointment(request):
    appointments = Appointment.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlist_appointment')
    else:
        form = AppointmentForm()
    return render(request, 'user_admin/user_book_appointment.html', {'form': form, 'appointments': appointments})


def user_update_appointment(request,appointment_id):

    appointments = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointments)

        if form.is_valid():
            form.save()

            return redirect('userlist_appointment')
    else:
        form = AppointmentForm(instance=appointments)

    return render(request, 'user_admin/user_update_appointment.html', {'form': form, 'appointments': appointments })

def userlist_appointment(request):
    appointments = Appointment.objects.all()


    return render(request,'user_admin/userlist.html',{'appointments':appointments })


def userdetails_appointment(request,appointment_id):
    appointments = Appointment.objects.get(id=appointment_id)

    return render(request,'user_admin/userdetails.html',{'appointments':appointments})


def deleteView(request,appointment_id):

    appointments = Appointment.objects.get(id=appointment_id)

    if request.method=='POST':
        appointments.delete()

        return redirect('userlist_appointment')



    return render(request,'user_admin/deleteview.html',{'appointments':appointments})





def facility_create(request):
    facilities = Facility.objects.all()
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlist')
    else:
        form = FacilityForm()
    return render(request, 'user_admin/facility_form.html', {'form': form, 'facilities': facilities})


def facility_update(request, facilities_id):
    facilities = Facility.objects.get(id=facilities_id)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facilities)
        if form.is_valid():
            form.save()
            return redirect('userlist')
    else:
        form = FacilityForm(instance=facilities)
    return render(request, 'user_admin/facility_form_update.html', {'form': form,'facilities': facilities})


def facility_delete(request, facilities_id):
    facilities = Facility.objects.get(id=facilities_id)
    if request.method == 'POST':
        facilities.delete()
        return redirect('userlist')
    return render(request, 'user_admin/facility_confirm_delete.html', {'facilities': facilities})


def facility_details(request,facilities_id):
    facilities = Facility.objects.get(id=facilities_id)

    return render(request,'user_admin/facilitydetails.html',{'facilities':facilities })




def user_detail(request, users_id):
    users = User.objects.get(id=users_id)
    return render(request, 'user_admin/users_detail.html', {'users': users})

def user_deleteView(request,users_id):

    users = User.objects.get(id=users_id)

    if request.method=='POST':
        users.delete()

        return redirect('userlist')



    return render(request,'user_admin/user_deleteview.html',{'users':users})