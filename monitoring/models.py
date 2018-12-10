from django.db import models
from datetime import timedelta


class Officer(models.Model):
    student_number = models.CharField(primary_key=True, null=False, max_length=7)
    first_name = models.CharField(max_length=128)
    middle_initial = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices=(('M', 'MALE'), ('F', 'FEMALE')))
    officer_type = models.CharField(max_length=5, choices=(('SSC', 'Supreme Student Council'), ('YLEAP', 'YLEAP')))
    cp_contact_number = models.CharField(max_length=11, null=True, blank=True)

    is_login = models.BooleanField(default=False, null=False)
    latest_login = models.DateTimeField(null=True, blank=True)
    latest_logout = models.DateTimeField(null=True, blank=True)
    weekly_time_spent = models.DurationField(null=False)
    daily_time_spent = models.DurationField(null=False)

    weekly_time_spent_hour = models.IntegerField(null=True, blank=True)
    weekly_time_spent_minutes = models.IntegerField(null=True, blank=True)
    daily_time_spent_hour = models.IntegerField(null=True, blank=True)
    daily_time_spent_minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Login(models.Model):
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    time_login = models.DateTimeField(null=False)
    time_logout = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)

    temp_stn = models.CharField(null=False, max_length=7, default="")

    def __str__(self):
        return str(self.time_login) + " " + str(self.officer)
