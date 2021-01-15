from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import *
router = routers.DefaultRouter()
router.register('service', ServiceViewSet, basename='service')
router.register('master', MasterViewSet, basename='master')
router.register('sertif', CertificatesViewSet, basename='sertif')
router.register('feed', FeedbackViewSet, basename='feed')



urlpatterns = [
    path('', include(router.urls)),

]
