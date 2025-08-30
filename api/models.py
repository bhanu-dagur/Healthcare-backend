from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_by = models.ForeignKey(User, related_name='patients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, related_name='mappings', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='mappings', on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"Patient {self.patient.id} <-> Doctor {self.doctor.id}"
