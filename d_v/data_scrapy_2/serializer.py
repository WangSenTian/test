# 北京工商大学
# 开发者： 薛浩杰
# 开发时间：2022/3/8 18:29
from rest_framework import serializers
from .models import xhj_sccs
class xhj_sccsSerializer(serializers.ModelSerializer):
    '''定义序列化器'''
    class Meta:
        model = xhj_sccs
        fields = '__all__'