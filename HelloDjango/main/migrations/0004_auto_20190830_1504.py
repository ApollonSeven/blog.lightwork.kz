# Generated by Django 2.2.4 on 2019-08-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_articles_meta_titile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='meta_titile',
        ),
        migrations.AddField(
            model_name='articles',
            name='meta_title',
            field=models.CharField(max_length=300, null=True, verbose_name='Title'),
        ),
    ]
