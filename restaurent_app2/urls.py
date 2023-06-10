from django.urls import path
from restaurent_app2 import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    
]