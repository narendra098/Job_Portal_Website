from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import Website_Users
import requests

# Create your views here.
def home(request):
    return render(request,'index.html')

def employee(request):
    return render(request,'employee.html')

def job_seeker(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        username = request.POST['your_name']
        mail = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        type_of_user = request.POST['type_of_user']
        
        userobj = Website_Users(name= name, user_name= username, mail=mail,password= password1,type_of_user=type_of_user)
        if password1 == password2:
            if Website_Users.objects.filter(user_name=username).exists():
                print('user already exists')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=name,email=mail)
                user.save()
                userobj.save()
                if type_of_user == 'employer':
                    auth.login(request,user)
            #msgs = 'welcome '+username
           # messages.info(request,msgs)
                    return redirect('emphome')
                else:
                    auth.login(request,user)
                    return redirect('userhome')


        else:
            print('password not matched')
    else:
        return render(request,'register.html')



def login(request):
     if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        userobj=Website_Users.objects.get(user_name=username)
        type_of_user = userobj.type_of_user
        print(type_of_user)
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if type_of_user == 'employer':
                auth.login(request,user)
            #msgs = 'welcome '+username
           # messages.info(request,msgs)
                return redirect('emphome')
            else:
                auth.login(request,user)
                return redirect('userhome')
        else:
            print('pass not valid ')
            return render(request,'login.html')
        
     else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    print('logged out')
    return redirect('index')

def job_listing(request):
    api_url = 'http://127.0.0.1:8000/view_jobs'
    available_jobs= requests.get(api_url)
    data = available_jobs.json()
    return render(request, 'job_listing.html',{'jobs':data})