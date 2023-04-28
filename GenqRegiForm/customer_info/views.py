from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
#from .models import customer_account
#from django.contrib.auth.models import Customer



# Create your views here.
def index(request):
    pr_title = 'GENQ KYC FORM'
    if request.user.is_authenticated:
        username = request.user.username
        return render(
            request,
            'index.html', 
            {'pr_title': pr_title, 'username':username}
        )
    else:
        author = 'Deborah_Patience'
        gender = 'Female'
        return render(
            request,
            'index.html', 
            {'pr_title': pr_title, 'author':author, 'gender':gender}
        ) 
        

def register(request):

    return render(request, 'register.html')

def registration(request):
    customer_Fname = request.POST['firstname']
    customer_Lname = request.POST['lastname']
    date_of_birth = request.POST['dateOfBirth']
    #password = request.POST['password']
    gender = request.POST['gender']
    customer_details=[
            customer_Fname,customer_Lname,date_of_birth,gender
        ]
    print(customer_details)
    if Customer.objects.filter(firstname=customer_Fname).first():
        print('Enter your first name here')
        return render(request, 'login.html')
    else:
        customer=Customer.objects.create_customer(customer_Fname, customer_Lname, date_of_birth, gender)
        return render(request, 'login.html')


def login_user(request):
    #here we handle data being posted from the login form
    customer_Fname = request.POST['firstname']
    customer_Lname = request.POST['lastname']
    date_of_birth = request.POST ['dateOfBirth']
    pwd = request.POST['password']
    #we check if the user already has an account in te database
    if Customer.objects.filter(customer_Fname='firstname'):
        print("Enter your first name here")
        #if the account exists we login using the username and password fields
        logged_user = authenticate(request, customer_Fname='firstname', customer_Lname='lastname', password=pwd)
        if logged_user is not None:
            #here we are logging in the user
            auth_login(request, logged_user)
            print(customer_Fname+" "+"Logged in successfuly")
            return redirect('index')
        else: 
            #here we handle a scenario where the authentication has failed
            return render(request, 'login.html')
    else:
        print("User Credentials do not exist.")
        return render(request, 'login.html')
    
def login_page(request):
    return render(request, 'login.html')

@login_required
def logout_user(request):
    auth_logout(request)
    return redirect('login_page')

