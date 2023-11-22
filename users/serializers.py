from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate (self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data