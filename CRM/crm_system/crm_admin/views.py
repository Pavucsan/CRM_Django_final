from django.shortcuts import render,redirect
from .models import customer
import datetime

from django.contrib import messages

# Create your views here.
now=datetime.datetime.now()
# Customer 
def index(request):
    cus=customer.objects.all()    
    return render(request,'index.html',{'option':1,'cus':cus})

def addCustomer(request):
    if request.method=='POST':
        id=request.POST['id']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        # photo=request
        email=request.POST['email']
        occupation=request.POST['occupation']
        phone=request.POST['phone']
        address=request.POST['address']
        date=now.strftime("%Y-%m-%d %H:%M")
        cust=customer(
            customer_id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            occupation=occupation,
            phone_number=phone,
            address=address,
            data_registration=date
        )
        cust.save()
        return redirect('/')
        # return render(request,'index.html',{'option':2})    
    return render(request,'index.html',{'option':2})

def editCustomer(request):
    if request.method=='POST':
        if request.POST['action']=='Search':
            fname=request.POST.get('fCustomer')
            if customer.objects.filter(first_name=fname).exists():
                cus=customer.objects.filter(first_name=fname)            
                return render(request,'index.html',{'option':3,'cus':cus})
            else:
                return render(request,'index.html',{'option':3,'msg':'Hello'})
        elif request.POST['action']=='Update':
            fname=request.POST.get('fname')
            cus=customer.objects.filter(first_name=fname)  

            ids=request.POST['ide']
            first_name=request.POST['fname']
            last_name=request.POST['lname']
            # email=request.POST['email']
            occupation=request.POST['occupation']
            phone=request.POST['phone']
            address=request.POST['address']
            date=now.strftime("%Y-%m-%d %H:%M")
            cus.update(customer_id=ids,
                first_name=first_name,
                last_name=last_name,
                # email=email,
                occupation=occupation,
                phone_number=phone,
                address=address,
                data_registration=date)
            return redirect('/')
    else:
        msg="Customer not exist!"
        return render(request,'index.html',{'option':3,'msg':msg})


def findCustomer(request):
    if request.method=='POST':
        fname=request.POST.get('fCustomer')
        if customer.objects.filter(first_name=fname).exists():
            cus=customer.objects.filter(first_name=fname)            
            return render(request,'index.html',{'option':1,'cus':cus})
        else:
            msg="Customer not exist!"
            return render(request,'index.html',{'option':1,'msg':msg})
        
def deleteCustomer(request):    
    if request.method=='POST':
        # if request.POST['fCustomer'].checked:
        fname=request.POST['fCustomer']    
        if customer.objects.filter(first_name=fname).exists():                
            msg=fname+' is deleted'
            cus=customer.objects.filter(first_name=fname) 
            cus.delete()
            return render(request,'index.html',{'option':1,'msg':msg})
        else:
            msg=fname+' is not exist in the customer table'
            return render(request,'index.html',{'option':1,'msg':msg})
    else:
        return render(request,'index.html',{'option':5})
    # else:
    #     msg="Customer not exist!"
    #     return render(request,'index.html',{'option':3,'msg':msg})


def cusCRUD(request):    
    if request.POST['action']=='Add':
        return addCustomer(request)
    elif request.POST['action']=='Search':
        return editCustomer(request)    
    elif request.POST['action']=='Delete':
        return deleteCustomer(request)  
    elif request.POST['action']=='Update':
        return editCustomer(request)
    elif request.POST['action']=='Find':
        return findCustomer(request)

    








# Product

# SalesMan

#Inventory