from dataclasses import fields
from rest_framework import serializers
from .models import Diary

class DiarySerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ["title","body","pub_date"]