# Generated by Django 3.2.9 on 2021-12-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0003_auto_20211214_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haha',
            name='category',
        ),
        migrations.RemoveField(
            model_name='haha',
            name='level',
        ),
        migrations.RemoveField(
            model_name='haha',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='haha',
            name='serviceCode',
        ),
        migrations.RemoveField(
            model_name='haha',
            name='sessiondId',
        ),
        migrations.AlterField(
            model_name='haha',
            name='size',
            field=models.IntegerField(),
        ),
    ]
