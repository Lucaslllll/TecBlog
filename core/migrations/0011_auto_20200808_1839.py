# Generated by Django 2.2.4 on 2020-08-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_users_logged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/foto_ads'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='media/foto_article'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/foto_users'),
        ),
    ]
