from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addCustomer',views.addCustomer,name='addCustomer'),
    path('editCustomer',views.editCustomer,name='editCustomer'),
    path('customer',views.index,name='customer'),
    path('findCustomer',views.findCustomer,name='findCustomer'),
    path('deleteCustomer',views.deleteCustomer,name='deleteCustomer')

    
]
