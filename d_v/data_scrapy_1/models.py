from django.db import models


class Content(models.Model):
    link = models.TextField(db_column="link",null=False)
    title = models.TextField(db_column="title",null=False)
    content = models.TextField(db_column="content",null=True)

    class Meta:
        managed = True
        db_table = 'Content'