# Generated by Django 3.2.12 on 2022-03-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_scrapy_4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='haiguan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=255)),
                ('attachment', models.TextField()),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
