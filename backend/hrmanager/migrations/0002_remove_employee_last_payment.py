# Generated by Django 3.2.7 on 2022-02-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='last_payment',
        ),
    ]
