from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet, MappingViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
