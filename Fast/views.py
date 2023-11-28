import sys
import random

from django.shortcuts import render, redirect
from Fast.forms import UserForm
from django.contrib import messages
from Fast.models import UserDetails
from Modern import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def show(request):
    return render(request, "SignIn_SignUp.html")


def calculator(request):
    return render(request, "Black_Calculator.html")


def insert_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(f"\n\n\n\n\n--------------------> {form.errors}")

        if form.is_valid():
            try:
                form.save()
                return redirect('/user_Signin_Signup')

            except:
                print(f"\n\n\n\n\n--------------------> {sys.exc_info()}")

    else:
        form = UserForm()

    return render(request, 'SignIn_SignUp.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        e = request.POST["email"]
        p = request.POST["password"]

        val = UserDetails.objects.filter(u_email=e, u_password=p).count()
        if val == 1:
            data = UserDetails.objects.filter(u_email=e, u_password=p)
            for item in data:
                request.session['user_id'] = item.u_id
                request.session['user_fname'] = item.u_fname
                request.session['user_lname'] = item.u_lname
                request.session['user_email'] = item.u_email
                request.session['user_pass'] = item.u_password

                if request.POST.get("remember"):
                    print("-----------------------------------------")
                    response = HttpResponseRedirect("/calc/")
                    # 3600 seconds in an hour
                    # 24 hours in a day
                    # 365 days in a year
                    # 2 year
                    e = request.POST["email"]
                    p = request.POST["password"]
                    response.set_cookie('cookie_u_email', e, max_age=3600, path='/')
                    response.set_cookie('cookie_u_password', p, max_age=3600, path='/')
                    return response
                else:
                    return HttpResponseRedirect('/calc/')
        else:
            messages.error(request, "Invalid Username or Password !!!")
            return redirect('/user_Signin_Signup/')
    else:
        return render(request, "SignIn_SignUp.html")


def user_forgot_password(request):
    return render(request, "Forgot_Password.html")


def user_otp(request):
    return render(request, "Otp.html")


def sendotp(request):
    otp1 = random.randint(10000, 99999)

    e = request.POST['fp_email']
    request.session['session_email'] = e

    obj = UserDetails.objects.filter(u_email=e).count()

    if obj == 1:

        UserDetails.objects.filter(u_email=e).update(otp=otp1, otp_used=0)
        subject = 'OTP Verification'
        message = str(f"{otp1} is your OTP to access calculator. "
                      f"\nFor security reasons, DO NOT share this OTP with anyone.")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'Otp.html')

    else:
        messages.error(request, "Invalid Email !!!")
        return render(request, "Forgot_Password.html")


def set_password(request):
    if request.method == "POST":

        email_otp = request.POST['u_otp']
        new_password = request.POST['u_new_password']
        confirm_cpass = request.POST['u_confirm_password']

        if new_password == confirm_cpass:

            e = request.session['session_email']
            val = UserDetails.objects.filter(u_email=e, otp=email_otp, otp_used=0).count()

            if val == 1:
                UserDetails.objects.filter(u_email=e).update(otp_used=1, u_password=new_password)
                return redirect("/user_Signin_Signup")
            else:
                messages.error(request, "Invalid OTP !!!")
                return render(request, "Otp.html")

        else:
            messages.error(request, "New password and Confirm password does not match !!!")
            return render(request, "Otp.html")

    else:
        return redirect("/forgot_password")
