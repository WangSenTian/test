from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from data_scrapy_1.models import Content
from data_scrapy_1.serializer import ContentSerializer


def get_contents(request):
    try:
        obj_content = Content.objects.all().values()
        print(obj_content[0])
        contents=list(obj_content)
        return JsonResponse({'code':1,'data':contents}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        return JsonResponse({'code':0,'msg':'异常'+str(e)})


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()  # 具体返回的数据
    print(queryset)
    serializer_class = ContentSerializer  # 指定过滤的类