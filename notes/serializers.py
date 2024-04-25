from .models import Notes
from rest_framework import serializers
from django.contrib.auth.models import User


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id','name', 'email', 'phone', 'address']