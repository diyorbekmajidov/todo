# Generated by Django 4.2 on 2023-09-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]