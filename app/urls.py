
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import Studentviewset,Rollviewset
router=DefaultRouter()
router.register(r'student',Studentviewset)
router.register(r'roll',Rollviewset)

urlpatterns = [
    path('',include(router.urls)),
]
