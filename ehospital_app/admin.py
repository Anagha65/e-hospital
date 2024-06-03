from django.contrib import admin

from ehospital_app.models import Patient, Doctor, MedicalHistory

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalHistory)

