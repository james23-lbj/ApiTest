# Generated by Django 2.0 on 2018-05-09 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180509_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='name',
        ),
    ]