# Generated by Django 3.2.6 on 2021-09-24 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20210924_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='new_cases',
            new_name='news_title',
        ),
        migrations.RemoveField(
            model_name='covid',
            name='New_cases',
        ),
        migrations.RemoveField(
            model_name='covid',
            name='Total_deaths',
        ),
        migrations.RemoveField(
            model_name='covid',
            name='Total_recovered',
        ),
        migrations.RemoveField(
            model_name='news',
            name='recovered_patients',
        ),
        migrations.RemoveField(
            model_name='news',
            name='recovery_percentage',
        ),
        migrations.RemoveField(
            model_name='news',
            name='tests_done',
        ),
        migrations.RemoveField(
            model_name='news',
            name='total_deaths',
        ),
        migrations.AddField(
            model_name='covid',
            name='new_cases',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='covid',
            name='recovered_patients',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='covid',
            name='recovery_percentage',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='covid',
            name='tests_done',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='covid',
            name='total_deaths',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.ImageField(null=True, upload_to='static/uploads'),
        ),
    ]
