from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):

    doc_name=models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.doc_name)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__ (self):
        return '{}'.format(self.patient)



class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()
    record_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.patient)

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])

    def __str__(self):
        return '{}'.format(self.patient)


class HealthEducationResource(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='health_media')
    description = models.TextField()
    link = models.URLField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)