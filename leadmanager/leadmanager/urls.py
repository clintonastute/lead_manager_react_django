from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # make sure the frontend loads before leads
    path('', include('frontend.urls')),
    path('', include('leads.urls'))
]
