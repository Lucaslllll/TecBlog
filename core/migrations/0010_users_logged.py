# Generated by Django 2.2.4 on 2020-08-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200808_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='logged',
            field=models.BooleanField(null=True),
        ),
    ]
