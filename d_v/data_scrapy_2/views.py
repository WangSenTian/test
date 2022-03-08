from django.shortcuts import render

# Create your views here.
from .models import xhj_sccs
from .serializer import xhj_sccsSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class xhj_sccsView(ModelViewSet):
    '''定义类试图'''
    # 指定查询集
    queryset = xhj_sccs.objects.all()
    # 指定序列化器
    serializer_class = xhj_sccsSerializer