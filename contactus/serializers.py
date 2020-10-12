  
from rest_framework import serializers
from contactus.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ('id','name','email','num','subject')