from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender','created_by','created_at')
    search_fields = ('name','phone')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','name','specialization','email','created_at')
    search_fields = ('name','specialization')

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id','patient','doctor','assigned_by','assigned_at')
    search_fields = ('patient__name','doctor__name')
