# Generated by Django 2.1.4 on 2019-10-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_articles_tag_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletags',
            name='slug',
            field=models.CharField(default='', max_length=100, verbose_name='Slug'),
        ),
    ]