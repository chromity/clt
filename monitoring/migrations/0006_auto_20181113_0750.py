# Generated by Django 2.1.3 on 2018-11-12 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_auto_20181113_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='time_login',
            field=models.DateTimeField(null=True),
        ),
    ]
