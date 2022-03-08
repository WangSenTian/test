from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from data_scrapy_3.models import WrcIccr
from data_scrapy_3.serializer import WrcIccrSerializer


def get_contents(request):
    try:
        obj_content = WrcIccr.objects.all().values()
        print(obj_content[0])
        contents=list(obj_content)
        return JsonResponse({'code':1,'data':contents})
    except Exception as e:
        return JsonResponse({'code':0,'msg':'异常'+str(e)})

class WrcIccrViewSet(viewsets.ModelViewSet):
    queryset = WrcIccr.objects.all()
    print(queryset)
    serializer_class = WrcIccrSerializer