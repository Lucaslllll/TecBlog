# Generated by Django 2.2.4 on 2020-08-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags4',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags5',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_send',
            field=models.DateField(),
        ),
    ]
