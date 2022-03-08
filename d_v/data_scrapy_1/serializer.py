from rest_framework import serializers
from .models import *


class ContentSerializer(serializers.ModelSerializer):
    # 声明数据
    class Meta:
        model = Content  # 要进行接口序列化的模型
        fields = ['link', 'title', 'content',]  # 序列要返回的字段