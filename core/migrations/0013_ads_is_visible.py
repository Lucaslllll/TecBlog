# Generated by Django 2.2.4 on 2020-08-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_article_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='is_visible',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
