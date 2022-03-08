from django.db import models

# Create your models here.
class xhj_sccs(models.Model):
   url = models.TextField(verbose_name='原链接', db_column="url", null=False, max_length=255)
   title = models.TextField(verbose_name='标题', db_column="title", max_length=255, null=False)
   document = models.TextField(verbose_name='文章链接', db_column="document", max_length=255, null=False)
   time = models.TextField(verbose_name='时间', db_column="time", max_length=255, null=False)

   class Meta:
       managed = True
       db_table = 'xhj_sccs'