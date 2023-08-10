from django.urls import path

from .views import DepozitDetails

urlpatterns = [
    path('',DepozitDetails.as_view(), name='detalii_depozit'),
]