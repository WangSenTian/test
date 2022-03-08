from django.db import models


class WrcIccr(models.Model):
    id = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wrc_iccr'

