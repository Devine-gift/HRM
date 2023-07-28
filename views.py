from django.shortcuts import render
from .models import Staff

# Create your views here.

def stafflogin(request):
    return render(request, 'staff/staffLogin.html')

 
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
       
        
        new_staff = Staff(firstname=firstname, lastname=lastname, address = address, dob=dob, email = email, password = password)
        new_staff.Save()
    return render(request,'staff/register.html' )

def staffdashboard(request):
    return render(request, 'staff/staff-dashboard.html')