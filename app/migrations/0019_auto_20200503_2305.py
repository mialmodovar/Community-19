# Generated by Django 2.2.12 on 2020-05-03 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200503_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='email_contact',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='tel_contact',
        ),
    ]
