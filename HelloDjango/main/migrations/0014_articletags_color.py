# Generated by Django 2.1.4 on 2019-10-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_articletags_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletags',
            name='color',
            field=models.CharField(default='', max_length=100, verbose_name='Цвет'),
        ),
    ]
