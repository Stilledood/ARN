from django.urls import path

from .views import RaftDetails

urlpatterns = [
    path('',RaftDetails.as_view(), name='detalii_raft'),
]