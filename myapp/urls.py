from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('otp/', views.otp, name='otp'),
    path('otp/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment/', views.payment, name='payment'),
   
]
