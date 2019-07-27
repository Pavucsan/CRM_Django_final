from django.db import models

# Create your models here.

class salesMan(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='pic')
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address=models.TextField()
    data_registration=models.DateTimeField(auto_now=False, auto_now_add=False)
    salesMan_id=models.IntegerField()
    dateOfBirth=models.DateField(auto_now=False, auto_now_add=False)
    territory=models.CharField(max_length=200)

class salesManPerformance(models.Model):
    salesMan_id=models.IntegerField()
    totSales=models.IntegerField()
    month_sale=models.IntegerField()
    year_sale=models.IntegerField()
    avg_sale=models.FloatField()

class product(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.FloatField()
    model=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='pic')
    date_add=models.DateTimeField(auto_now=False, auto_now_add=False)

class inventory(models.Model):
    product_id=models.IntegerField()
    stock_status=models.BooleanField()
    date_time=models.DateTimeField( auto_now=False, auto_now_add=False)

class customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='pic')
    email=models.EmailField(max_length=254)
    occupation=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address=models.TextField()
    data_registration=models.DateTimeField()
    customer_id=models.IntegerField()

class complain(models.Model):
    detail=models.TextField()
    status=models.BooleanField("Fales")
    technician=models.CharField(max_length=50)
    compline_date=models.DateTimeField(auto_now=False, auto_now_add=False)

class sale(models.Model):
    amount=models.FloatField()
    qty=models.FloatField()
    billId=models.IntegerField()
    product_id=models.IntegerField()

class bill(models.Model):
    billId=models.IntegerField()
    billDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    customer_id=models.IntegerField()





