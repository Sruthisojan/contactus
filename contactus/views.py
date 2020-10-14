

#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .serializers import ContactSerializer

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from contactus.models import Contact
from contactus.serializers import ContactSerializer
from rest_framework.decorators import api_view
# Create your views here.


def contact(request):
    contacts=Contact.objects.all()
    template='index.html'
    return render(request,template,{'contactlists':contacts})


def index(request):
    if request.method=="POST":
        contactus=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        num=request.POST.get('num')
        subject=request.POST.get('subject')
        contactus.name=name
        contactus.email=email
        contactus.num=num
        contactus.subject=subject
        contactus.save()
    return render(request,'index.html')
@csrf_exempt
@api_view(["GET","POST"])
def contact_us(request):
    if request.method=="GET":
        contactus=Contact.objects.all()
        name=request.GET.get('name',None)
        if name is not None:
            contactus=contactus.filter(name__icontains=name)
        serializer=ContactSerializer(contactus, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method=="POST":
        print(request.data)
        try:
            contactdata=JSONParser().parse(request)
        except Exception as e:
            print(e)
        
        print(contactdata)
        serializer=ContactSerializer(data=contactdata)
        
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        print (serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


   
