# Generated by Django 2.2.12 on 2020-05-14 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20200514_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='yt_link',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
