# Generated by Django 3.2.6 on 2021-09-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_title',
            field=models.TextField(null=True),
        ),
    ]
