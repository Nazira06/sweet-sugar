from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.




class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers


class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializers


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers