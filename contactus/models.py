from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
#    num=models.BigIntegerField()
    subject=models.TextField()
    
    class Meta:
        ordering=('id',)
    def __str__(self):
        return self.name