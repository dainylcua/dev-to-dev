# Generated by Django 3.2.9 on 2021-11-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='date_published'),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
