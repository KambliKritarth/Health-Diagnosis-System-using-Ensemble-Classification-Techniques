from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('covid',views.covid, name = "covid"),
    path('heartdisease',views.heartdisease, name = "heartdisease"),
    path('diabetes',views.diabetes, name = "diabetes"),
    path('submitmyform',views.submitmyform,name = 'submitmyform'),
]