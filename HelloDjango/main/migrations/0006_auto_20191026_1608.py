# Generated by Django 2.1.4 on 2019-10-26 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_articles_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='tag_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ArticleTags'),
        ),
    ]
