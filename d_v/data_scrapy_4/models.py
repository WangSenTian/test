from django.db import models

# class UserInfo(models.Model):
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=64)
#     age = models.IntegerField(default=2)
#
#
# class Department(models.Model):
#     title = models.CharField(max_length=16)

class haiguan(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.CharField(max_length=255)
    attachment = models.TextField()
    url = models.CharField(max_length=255)