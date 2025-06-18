from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register_view,name='register' ),
    path('login/',views.Login_view,name='login'),
    path('login/otp/', views.login_with_otp, name='login_with_otp'),
    path('logout/',views.Logout_view,name='logout'),
    path('home/',views.Home_view,name='home'),
    path('identify/', views.identifyview, name='identifyuser'),
    path('resetpassword/<str:en_name>/', views.resetpassword, name='resetpassword'),
    path('otp/<str:enc_name>/',views.OTP_View,name='otp_view'),
    path('resend-otp/<str:enc_name>/', views.resend_otp, name='resend_otp'),
]