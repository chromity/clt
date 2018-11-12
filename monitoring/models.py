from django.db import models


class Officer(models.Model):
    student_number = models.CharField(null=False, max_length=7)
    first_name = models.CharField(max_length=128)
    middle_initial = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices=(('M', 'MALE'), ('F', 'FEMALE')))
    cp_contact_number = models.CharField(max_length=11)

    is_login = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Login(models.Model):
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    time_login = models.DateTimeField(null=False)
    time_logout = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)

    def __str__(self):
        return str(self.time_login) + " " + str(self.officer)
