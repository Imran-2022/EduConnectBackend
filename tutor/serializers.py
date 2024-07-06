from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class TutorSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    
    class Meta:
        model = models.Tutor
        fields='__all__'

    def create(self, validated_data):
        return models.Tutor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.description = validated_data.get('description', instance.description)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.educational_qualification = validated_data.get('educational_qualification', instance.educational_qualification)
        instance.save()
        return instance

class RegistrationSerializer(serializers.ModelSerializer):

    # comfirm password ar jonno ekta serializer toire krte hbe..! 
    confirm_password=serializers.CharField(required=True)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

        # build in. 

        # now check match comfirm pass equal pass && same email dea kno user nai.

        
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['confirm_password']
        # cleaned_data 

        if password!=password2:
            raise serializers.ValidationError({"error":"Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"Email already exit"})
        
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        print(account)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
