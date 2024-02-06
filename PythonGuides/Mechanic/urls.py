from django.urls import path
from .views import *

urlpatterns = [
    path('signup_mech',signup_mech,name='signup_mech'),
    path('mech_details',mech_details,name='mech_details'),
    path('mech_login',mech_login,name='mech_login'),
    path('update_map',update_map,name='update_map'),
    path('get_card_data',get_card_data,name='get_card_data'),
    path('get_vehicle_data',get_vehicle_data,name='get_vehicle_data'),
    path('mechanic/next_page',next_page,name='next_page'),
    path('mech_dashboard',mech_dashboard,name='mech_dashboard'),
    path('display_info/<str:username>/',display_info,name='display_info'),
    path('home_page',home_page,name='home_page'),
    path('logout_mech',logout_mech,name='logout_mech'),
    path('mech_profile',mech_profile,name='mech_profile'),
    path('mech_feedback',mech_feedback,name='mech_feedback'),
    path('mech_bookings',mech_bookings,name='mech_bookings'),
    path('mech_resolved',mech_resolved,name='mech_resolved'),
    path('mech_unresolved',mech_unresolved,name='mech_unresolved'),
    path('mech_forgot_password',mech_forgot_password,name='mech_forgot_password'),
    path('mech_otp_forgot_passwd',mech_otp_forgot_passwd,name='mech_otp_forgot_passwd'),
    path('ongoing_booking',ongoing_booking,name='ongoing_booking'),
    path('verify_email_otp',verify_email_otp,name='verify_email_otp'),


    
]

