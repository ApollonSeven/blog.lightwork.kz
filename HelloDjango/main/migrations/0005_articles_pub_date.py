# Generated by Django 2.1.4 on 2019-10-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190830_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]