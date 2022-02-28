from django.db import models

# Create your models here.

class UserAccount(models.Model):
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
    email=models.EmailField(max_length=25,unique=True)
    web=models.URLField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.first_name
