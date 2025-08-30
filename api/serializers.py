from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping

class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('name','email','password')

    def create(self, validated_data):
        name = validated_data.pop('name')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        return user

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by','created_at')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_at',)

class MappingSerializer(serializers.ModelSerializer):
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')

    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ('assigned_by','assigned_at')
