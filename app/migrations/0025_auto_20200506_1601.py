# Generated by Django 2.2.12 on 2020-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_post_yt_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile2.png', upload_to=''),
            preserve_default=False,
        ),
    ]
