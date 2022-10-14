# Generated by Django 2.2.12 on 2020-04-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='contact',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
    ]
