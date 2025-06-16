from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import RegisterForm,LoginForm,IdentifyUser
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from .models import User
import random
from django.utils import timezone

from .utils import get_otp, enc_uname, dec_uname


# Create your views here.
def Register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            fname= form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            send_mail(
                'Account created successfully',
                'Hello ' + fname + ' ' + lname + ',\n\n' +
                'Your account has been created successfully.\n\n' +
                'Thank you for registering with us.\n\n' +
                'Best regards,\n' +
                'Tech Febric',
                'kiranmoymahanty@gmail.com',
                [email],
                fail_silently=True
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('home')
        messages.error(request, 'Invalid username or password.')
        # return HttpResponse ('invalid user')
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def Logout_view(request):
    logout(request)
    messages.error(request, "You have been logged out")
    return redirect('login')
def Home_view(request):
    return render(request, 'accounts/home.html')

# def identifyview(request):
#     if request.method == 'POST':
#         form = IdentifyUser(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             try:
#                 user = User.objects.get(username=username)
#                 en_uname = urlsafe_base64_encode(force_bytes(username))
#                 reset_url = f"http://127.0.0.1:8000/resetpassword/{en_uname}/"

#                 subject = 'TechTurtle - Password Reset'
#                 message = f"""
#                 Hello {user.username},

#                 We received a request to reset your password.

#                 Click the link below to reset your password:
#                 {reset_url}

#                 If you did not request this, please ignore this email.

#                 Regards,
#                 TechTurtle Team
#                 """
#                 from_email = settings.EMAIL_HOST_USER
#                 send_mail(subject, message.strip(), from_email, [user.email])

#                 messages.success(request, 'A password reset link has been sent to your email.')
#                 return redirect('login')
#             except User.DoesNotExist:
#                 messages.error(request, 'No user found with that username.')
#     else:
#         form = IdentifyUser()
#     return render(request, 'accounts/identifyuser.html', {'form': form})


# def resetpassword(request, en_name):
#     try:
#         dc_ename = force_str(urlsafe_base64_decode(en_name))
#         user = User.objects.get(username=dc_ename)
#     except (User.DoesNotExist, ValueError, TypeError):
#         messages.error(request, 'Invalid or expired reset link.')
#         return redirect('identifyuser')

#     if request.method == 'POST':
#         form = SetPasswordForm(user=user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Password reset successfully!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Failed to reset password.')
#     else:
#         form = SetPasswordForm(user=user)

#     return render(request, 'accounts/password_update.html', {'form': form})

def identifyview(request):
    if request.method == 'POST':
        form = IdentifyUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                # otp = str(random.randint(100000, 999999))
                # request.session['otp'] = otp
                # request.session['username'] = username
                otp =get_otp()
                time = timezone.now() + timezone.timedelta(minutes=5)
                user.otp = otp
                user.otp_expire = time
                user.save()
                send_mail(
                    subject='Your OTP for Password Reset',
                    message=f'Hi {user.first_name},\n\nYour OTP is: {otp}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                messages.success(request,'OTP has been sent to your registered email.')
                enc_name = enc_uname(username)
                url= f"/accounts/otp/{enc_name}/"
                return redirect('otp_view', enc_name=enc_name)
            messages.error(request,'user not found')
    context={
        'form': IdentifyUser()
    }
    return render(request,'accounts/identifyuser.html',context)

def OTP_View(request,enc_name):
    username = dec_uname(enc_name)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        # Assume expected OTP stored in session
        expected_otp = request.session.get('otp')

        if entered_otp == expected_otp:
            messages.success(request, "OTP verified successfully!")
            return redirect('home')  # or any other success URL
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'accounts/otp.html')

          