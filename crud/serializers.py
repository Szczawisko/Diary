from dataclasses import fields
from rest_framework import serializers
from .models import Diary

class DiarySerialaizer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.version = instance.version + 1
        return super().update(instance, validated_data)

    class Meta:
        model = Diary
        fields = ["id","title","body","pub_date"]