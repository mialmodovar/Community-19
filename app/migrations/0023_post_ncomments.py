# Generated by Django 2.2.12 on 2020-05-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_post_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ncomments',
            field=models.IntegerField(default=0),
        ),
    ]