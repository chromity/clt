# Generated by Django 2.1.2 on 2018-11-13 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_login', models.DateTimeField()),
                ('time_logout', models.DateTimeField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('temp_stn', models.CharField(default='', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('student_number', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('middle_initial', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('officer_type', models.CharField(choices=[('SSC', 'Supreme Student Council'), ('YLEAP', 'YLEAP')], max_length=5)),
                ('cp_contact_number', models.CharField(blank=True, max_length=11, null=True)),
                ('is_login', models.BooleanField(default=False)),
                ('latest_login', models.DateTimeField(blank=True, null=True)),
                ('latest_logout', models.DateTimeField(blank=True, null=True)),
                ('weekly_time_spent', models.DurationField()),
                ('daily_time_spent', models.DurationField()),
                ('weekly_time_spent_hour', models.IntegerField(blank=True, null=True)),
                ('weekly_time_spent_minutes', models.IntegerField(blank=True, null=True)),
                ('daily_time_spent_hour', models.IntegerField(blank=True, null=True)),
                ('daily_time_spent_minutes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='officer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.Officer'),
        ),
    ]
