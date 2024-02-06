from django.urls import path
from .views import *

urlpatterns = [
    path("",home_page,name='home_page'),
    path("home_page",home_page,name='home_page'),
    path('navbar', navbar, name='navbar'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('save_location',save_location,name='save_location'),
    path('BookMechanic',BookMechanic,name='BookMechanic'),
    path('loc',loc,name="loc"), 
    path('vehicle_details',vehicle_details,name="vehicle_details"), 
    path('accept_rules',accept_rules,name="accept_rules"),
    path('check_mechanic',check_mechanic,name='check_mechanic'),
    path('mech_booked',mech_booked,name="mech_booked"),
    path('profile',profile,name="profile"),
    path('waiting_page',waiting_page,name="waiting_page"),
    path('feedback',feedback,name="feedback"),
    path('logout_cust',logout_cust,name="logout_cust"),
    path('Booking_histroy',Booking_histroy,name="Booking_histroy"),
    path('otp',otp,name="otp"),
    path('forgot_password',forgot_password,name="forgot_password"),
    path("otp_forgot_passwd",otp_forgot_passwd,name="otp_forgot_passwd"),
    path("check_booking_status",check_booking_status,name="check_booking_status"),
]