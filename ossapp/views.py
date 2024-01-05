from django.shortcuts import render, redirect
from django.db import models
from . models import Customer






def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def rd(request):
    return render(request,'rd.html')
def blog(request):
    return render(request,'blog.html')
def room10(request):
    return render(request,'room10.html')
def room(request):
    return render(request,'room.html')
def room2(request):
    return render(request,'room2.html')
def room3(request):
    return render(request,'room3.html')
def room4(request):
    return render(request,'room4.html')
def room5(request):
    return render(request,'room5.html')
def room6(request):
    return render(request,'room6.html')
def room7(request):
    return render(request,'room7.html')
def room8(request):
    return render(request,'room8.html')
def base(request):
    return render(request,'base.html')
def checkout(request):
    return render(request,'checkout.html')
def room9(request):
    return render(request,'room9.html')


def book(request):
    if request.method == 'POST':
            err = None
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            name = request.POST.get('name')
            age = request.POST.get('age')
            person = request.POST.get('person')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone1 = request.POST.get('phone2')
            phone2 = request.POST.get('phone1')
            gender = request.POST.get('gender')
            selectstate = request.POST.get('state')
            selectcity = request.POST.get('city')

            # Validation
            values = {'checkin': checkin,
                      'checkout': checkout,
                      'name': name,
                      'age': age,
                      'person': person,
                      'phone2': phone2,
                      'email': email,
                      'address': address,
                      'phone1': phone1,
                      'gender': gender,
                      'selectstate': selectstate,
                      'selectcity': selectcity,
                      }


            myuser= Customer(checkin=checkin, checkout=checkout, name=name, age=age, person=person, phone1=phone1,
                                  gender=gender, address=address, phone2=phone2, email=email,
                                  selectcity=selectcity, selectstate=selectstate)
            myuser.save()


    return render(request,'book.html')















