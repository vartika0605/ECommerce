# Generated by Django 2.2 on 2020-09-09 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200910_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ref_code',
        ),
    ]
