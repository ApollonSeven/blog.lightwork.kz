# Generated by Django 2.1.4 on 2019-10-26 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191026_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletags',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='tag_new',
        ),
        migrations.AddField(
            model_name='articles',
            name='tag_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ArticleTags'),
        ),
    ]
