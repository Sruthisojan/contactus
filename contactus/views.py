from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer

# Create your views here.

def index(request):
    if request.method=="GET":
        contactlist=Contact.objects.all()
        serializer=ContactSerializer(contactlist, many=True)
        return Response(serializer.data)

    return render(request,'index.html')
