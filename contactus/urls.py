from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    url(r'^api/contactus$',views.index,name='index'),
    
]
