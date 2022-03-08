from rest_framework import serializers
from .models import WrcIccr


class WrcIccrSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrcIccr
        fields = [
            'id',
            'link',
            'title',
            'text',
        ]