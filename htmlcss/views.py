import email
from email import message
from multiprocessing import context
from django import views
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Member, Profile
from .forms import FormRegisterForm, LoginForm
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages 
from django.contrib.sites.shortcuts import get_current_site
# from .models import User
def index(request):
        return render(request, 'index.html')


def send_email_after_registration(request,email, token):
        current_site = get_current_site(request)
        subject = "Verify Email"
        message = f'Hi Click on the link to verify your account {current_site.domain}/account_verify/{token}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


def registration(request):
        
        if request.method == "POST":

                user_obj=Member.objects.filter(email=request.POST.get('email'))
                
                if user_obj:
                        messages.info(request, 'Email already exist')
                        cform = FormRegisterForm()
                        context = {'cform':cform}
                        return render(request, 'Registration.html', context)
                        
                else:
                        
                        cform = FormRegisterForm(request.POST)
                        if cform.is_valid():
                                username1 = request.POST.get('username')
                                funame1 = request.POST.get('funame')
                                email1 = request.POST.get('email')
                                mobile1 = request.POST.get('mobile')
                                pass11 = request.POST.get('password')
                                pass21 = request.POST.get('confirm_Password')

                                if pass11 is not None and pass11 != pass21:  
                                        messages.success(request,"Your passwords dose not must match")
                                        context = {'cform':cform}
                                        return render(request, 'Registration.html', context)
                        
                                data = Member(
                                        username = username1,
                                        funame = funame1,
                                        email = email1,
                                        mobile = mobile1,
                                        password = pass11,
                                        confirm_Password = pass21
                                )
                                data.save()
                                member=Member.objects.filter(email=request.POST.get('email'))[0]
                                uid = uuid.uuid4()
                                save_profile=Profile(user=member,
                                                token=uid)
                                save_profile.save()



                                send_email_after_registration(request,member.email, uid)
                                # messages.success(request, "Your Account Created Successful, To Verify Your Account Check your Email")
                                return redirect('/SendE/')
                        
        else:   
                cform = FormRegisterForm()
                context = {'cform':cform}
                return render(request, 'Registration.html', context)
                
def acccount_verify(request, token):
        pf = Profile.objects.filter(token=token).first()
        pf.verify = True
        pf.save()
        return redirect('/login/')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                
        
                user_obj = Member.objects.filter(username = username).first()
                if user_obj is None:
                        messages.success(request, 'User not found.')
                        return redirect('/login/')
                
                profile_obj = Profile.objects.filter(user = user_obj ).first()
                if not profile_obj.verify:
                        messages.success(request, 'Profile is not verified check your mail.')
                        return redirect('/login/')
                
                # password_obj = Member.objects.filter(password = password)

                # print(password_obj)

                user = Member.objects.filter(username=request.POST.get('username'),password=request.POST.get('password'))
                
                if not user:
                        messages.success(request, 'Wrong password.')
                        return redirect('/login/')
                # fm = username

                request.session['username'] = username

                # return render(request,"/profile/profile/")
                return redirect("/profile/profile/")
                
        else:
                fm = LoginForm()
                return render(request, 'Login.html', {'form':fm})

def SendE(request):
        return render(request, 'SendE.html')

def about(request):
        return render(request, "About.html")
        
def contact(request):
        return render(request, "contact.html")