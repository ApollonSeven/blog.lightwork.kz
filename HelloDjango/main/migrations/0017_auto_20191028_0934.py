# Generated by Django 2.1.4 on 2019-10-28 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_articles_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='tag_new',
            new_name='tag',
        ),
    ]
