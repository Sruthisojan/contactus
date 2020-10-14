from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('create', views.create_user,name='create'),
    path('', views.contact, name='contact'),
    url(r'^api/contactus$',views.contact_us,name='contact_us'),  
]
