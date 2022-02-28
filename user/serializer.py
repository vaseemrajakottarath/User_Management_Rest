from .models import UserAccount
from rest_framework  import fields,serializers

class UserRegister(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields=['id','first_name','last_name','company_name','city','state','zip','email','web','age']

class UserDetails(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields=['id','first_name','last_name','company_name','city','state','zip','email','web','age']
