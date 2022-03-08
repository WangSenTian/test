"""d_v URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from data_scrapy_1 import views
from data_scrapy_3 import views
from django.urls import path
from data_scrapy_1.views import *
from data_scrapy_3.views import *
from django.conf.urls import url,include
from data_scrapy_2.views import *
from data_scrapy_2 import views

from rest_framework.routers import DefaultRouter
from data_scrapy_4.views import HaiguanView


router = routers.DefaultRouter()
router.register(r'iccr',WrcIccrViewSet)
router.register(r'Content', ContentViewSet)
router.register(r'data_scrapy_4',HaiguanView,basename='data_scrapy_4')
router.register(r'sccs', views.xhj_sccsView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('iccr/', include(router.urls)),
    path('jcia/', include(router.urls)),
    path('wyj/', include(router.urls)),
    path('sccs/', include(router.urls)),
]


