# Generated by Django 3.2 on 2023-05-31 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('campaign', '0006_auto_20230522_2035'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Block',
        ),
    ]
