# Generated by Django 2.2.4 on 2020-08-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200808_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_visible',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
