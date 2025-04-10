
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import Studentviewset
router=DefaultRouter()
router.register(r'student',Studentviewset)

urlpatterns = [
    path('',include(router.urls)),
]
