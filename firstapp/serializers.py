from django import forms
from django.forms import fields
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields = '__all__'
        # fields = ['name','email','phone','subject','details']

# Django forms
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model= Contact
#         fields= '__all__'   




class ContactSerializerOne(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200)
    details = serializers.CharField(max_length=200)
    
    def create(self,validated_data):
        return Contact(**validated_data)
    
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.details = validated_data.get('details',instance.details)
        instance.save()
        return instance


