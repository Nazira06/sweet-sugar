from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Service, Master, Certificates, Feedback




class CertificatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ['id', 'image', 'name', 'level', 'master', 'date']

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'author', 'text', 'master']


class ServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['id', 'image', 'name', 'description', 'price', 'master']

class ServiceList(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']

class MasterCertificateList(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ['id', 'name']


class MasterSerializers(serializers.ModelSerializer):
    certificate = MasterCertificateList(many=True)
    service = ServiceList(many=True)
    class Meta:
        model = Master
        fields = ['id', 'image', 'name', 'exp', 'certificate', 'service']



