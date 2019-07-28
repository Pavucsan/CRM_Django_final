from django.shortcuts import render,redirect
from .models import customer
import datetime

from django.contrib import messages

class classCustomer:
    # Create your views here.
    def __init__(self):
        self.now=datetime.datetime.now()
    
    # Customer 
    def index(self,request):
        cus=customer.objects.all()    
        return render(request,'index.html',{'option':1,'cus':cus})

    def addCustomer(self,request):
        try:
            if request.method=='POST':
                id=request.POST['id']
                first_name=request.POST['fname']
                last_name=request.POST['lname']
                # photo=request
                email=request.POST['email']
                occupation=request.POST['occupation']
                phone=request.POST['phone']
                address=request.POST['address']
                date=self.now.strftime("%Y-%m-%d %H:%M")
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
        
        except Exception as e:
            return render(request,'index.html',{'option':1,'msg':e})

    def editCustomer(self,request):
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
                date=self.now.strftime("%Y-%m-%d %H:%M")
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


    def findCustomer(self,request):
        if request.method=='POST':
            if request.POST['action']=='Find':
                fname=request.POST.get('fCustomer')
                if customer.objects.filter(first_name=fname).exists():
                    cus=customer.objects.filter(first_name=fname)            
                    return render(request,'index.html',{'option':1,'cus':cus})
                else:
                    return render(request,'index.html',{'option':1})
            else:
                msg="Customer not exist!"
                return render(request,'index.html',{'option':1,'msg':msg})
            
    def deleteCustomer(self,request):    
        if request.method=='POST':
            # if request.POST['fCustomer'].checked:
            fname=request.POST['fCustomer']  
            if  request.POST['action']=='FindD':  
                if customer.objects.filter(first_name=fname).exists():            
                    cus=customer.objects.filter(first_name=fname)            
                    return render(request,'index.html',{'option':5,'cus':cus,'fname':fname})     
                else:   
                    return render(request,'index.html',{'option':5,'fname':fname})         
            elif  request.POST['action']=='Delete':  
                if customer.objects.filter(first_name=fname).exists():            
                    cus=customer.objects.filter(first_name=fname)  
                    msg=fname+' is deleted'
                    cus.delete()
                    return render(request,'index.html',{'option':5,'msg':msg})
                # return redirect('/')
            else:
                msg=fname+' is not exist in the customer table'
                return render(request,'index.html',{'option':5,'msg':msg,'fname':''})
        else:
            return render(request,'index.html',{'option':5})
        
    def cusCRUD(self,request):    
        if request.POST['action']=='Add':
            return self.addCustomer(request)

        elif request.POST['action']=='Search':
            return self.editCustomer(request)    

        elif request.POST['action']=='Delete':
            return self.deleteCustomer(request)  

        elif request.POST['action']=='Update':
            return self.editCustomer(request)

        if request.POST['action']=='Find':
            return self.findCustomer(request)

        if request.POST['action']=='FindD':
            return self.deleteCustomer(request)

class classSalesMan:
    pass


class classInventry:
    pass








# Product

# SalesMan

#Inventory