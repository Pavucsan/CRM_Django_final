from django.urls import path
from .views import classCustomer

from . import views


# object for customer class
customer=classCustomer()

urlpatterns = [
    path('',customer.index,name='index'),
    path('addCustomer',customer.addCustomer,name='addCustomer'),
    path('editCustomer',customer.editCustomer,name='editCustomer'),
    path('customer',customer.index,name='customer'),
    path('findCustomer',customer.findCustomer,name='findCustomer'),
    path('deleteCustomer',customer.deleteCustomer,name='deleteCustomer'),
    path("cusCRUD", customer.cusCRUD, name="cusCRUD")

    
]
