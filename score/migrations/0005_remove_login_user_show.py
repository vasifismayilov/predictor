# Generated by Django 4.1.4 on 2022-12-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0004_login_user_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_user',
            name='show',
        ),
    ]