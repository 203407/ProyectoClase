
from rest_framework import serializers
from django.contrib.auth.models import User
""" from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password """


class FirstSerializerRegister(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    