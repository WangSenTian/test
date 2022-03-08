from rest_framework import serializers
from .models import haiguan

class HaiguanSerializer(serializers.ModelSerializer):
    class Meta:
        model = haiguan
        fields = ['title','content','date','attachment','url']