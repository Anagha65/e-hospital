from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.patient_registration, name='patient_registration'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
path('create_doctor/', views.create_doctor, name='create_doctor'),
path('update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('medical_history/', views.create_medical_history, name='medical_history'),
path('update_medical_history/<int:history_id>/', views.update_medical_history, name='update_medical_history'),
path('medical_history_details/<int:history_id>/', views.medical_history_details, name='medical_history_details'),
path('add_billing/', views.add_billing, name='add_billing'),
path('update_billing/<int:billing_id>/', views.update_billing, name='update_billing'),

path('add_resource/', views.add_health_education_resource, name='add_resource'),
path('update_resource/<int:resource_id>/', views.update_health_educational_resource, name='update_resource'),
path('details_resource/<int:resource_id>/', views.resource_details, name='details_resource'),


path('create_checkout_session/<int:billing_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/<int:billing_id>/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),


# path('login/', views.user_login, name='login'),

]
