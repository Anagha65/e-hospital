
from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
path('create_doctors/',views.create_doctor, name='create_doctors'),
path('',views.doctorslist, name='doctors_list'),

path('doctors_details/<int:doctors_id>/',views.userdetails_doctor, name='doctors_details'),
path('delete_doctors/<int:doctors_id>/',views.doctor_deleteView, name='delete_doctors'),
path('update_doctors/<int:doctors_id>/',views.doctor_update_view, name='update_doctors'),

path('appoinment_details_doctor/<int:appointment_id>/',views.appoinment_details_doctor, name='appoinment_details_doctor'),


path('create_prescription',views.create_prescription, name='create_prescription'),
path('prescription_details/<int:prescriptions_id>/',views.prescription_details, name='prescription_details'),






]
