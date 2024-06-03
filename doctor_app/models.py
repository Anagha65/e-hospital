from django.db import models

from ehospital_app.models import Doctor, Patient


# Create your models here.


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.TextField()
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    prescribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.patient)


