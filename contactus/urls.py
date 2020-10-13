from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('first', views.index,name='index'),
    path('', views.contact, name='contact'),
    url(r'^api/contactus$',views.contact_us,name='contact_us'),  
]
