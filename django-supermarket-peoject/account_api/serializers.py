from rest_framework import serializers
from account_api.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        