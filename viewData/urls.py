from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('viewStateData/', viewState,name='state_url'),
    path('viewDistrictData/<id>/', viewDistrict,name='district_url'),
    path('viewTalukaData/', viewTaluka,name='taluka_url')
]
