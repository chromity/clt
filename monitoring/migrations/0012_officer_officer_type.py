# Generated by Django 2.1.3 on 2018-11-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0011_auto_20181113_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='officer_type',
            field=models.CharField(choices=[('SSC', 'Supreme Student Council'), ('YLEAP', 'YLEAP')], default='SSC', max_length=4),
            preserve_default=False,
        ),
    ]