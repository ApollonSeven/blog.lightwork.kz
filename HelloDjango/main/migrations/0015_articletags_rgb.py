# Generated by Django 2.1.4 on 2019-10-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_articletags_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletags',
            name='rgb',
            field=models.CharField(default='', max_length=100, verbose_name='RGB'),
        ),
    ]