from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer, UserRegisterSerializer
class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Doctor.objects.all()

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PatientDoctorMapping.objects.all()

    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        if patient.created_by != self.request.user:
            raise PermissionDenied("You can only assign doctors to your own patients.")
        serializer.save(assigned_by=self.request.user)

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_for_patient(self, request, patient_id=None):
        mappings = self.get_queryset().filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
