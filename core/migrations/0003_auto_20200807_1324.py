# Generated by Django 2.2.4 on 2020-08-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_update',
            field=models.DateField(blank=True, null=True),
        ),
    ]