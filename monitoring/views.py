from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from .forms import *
import logging
from django.http import HttpResponse


# enable logging in this application
logger = logging.getLogger(__name__)


@login_required(login_url='admin:login')
def index(request):
    return render(request, 'monitoring/index.html')


@login_required(login_url='admin:login')
def login(request):
    officer_data = Officer.objects.order_by('-latest_login')

    if request.method == "POST":
        officer_obj = get_object_or_404(Officer, student_number=request.POST['temp_stn'])

        if officer_obj.is_login:
            login_obj = Login.objects.filter(officer=officer_obj).latest("time_login")
            time = datetime.now(timezone.utc)

            # compute login duration
            duration = time - login_obj.time_login

            # compute weekly time spent, add it to existing computation
            if officer_obj.weekly_time_spent is None:
                weekly_time_spent = duration
            else:
                weekly_time_spent = officer_obj.weekly_time_spent + duration

            if officer_obj.daily_time_spent is None:
                daily_time_spent = duration
            else:
                daily_time_spent = officer_obj.daily_time_spent + duration

            # compute display variables
            weekly_time_spent_hours = weekly_time_spent.total_seconds() // 3600
            weekly_time_spent_minutes = (weekly_time_spent.total_seconds() % 3600) // 60
            daily_time_spent_hours = daily_time_spent.total_seconds() // 3600
            daily_time_spent_minutes = (daily_time_spent.total_seconds() % 3600) // 60

            # save the final model
            Officer.objects.filter(student_number=request.POST['temp_stn']).update(
                weekly_time_spent=weekly_time_spent,
                daily_time_spent=daily_time_spent,
                latest_logout=time,
                is_login=False,
                weekly_time_spent_hour=weekly_time_spent_hours,
                weekly_time_spent_minutes=weekly_time_spent_minutes,
                daily_time_spent_hour=daily_time_spent_hours,
                daily_time_spent_minutes=daily_time_spent_minutes)

            # update officer object
            Login.objects.filter(time_login=officer_obj.latest_login).update(time_logout=time, duration=duration)

        else:
            form = LoginForm(request.POST)
            time = datetime.now()

            # create login event record
            login_event = form.save(commit=False)
            login_event.officer = officer_obj
            login_event.time_login = time
            login_event.temp_stn = request.POST['temp_stn']

            # save login event to database
            login_event.save()

            # update officer object
            Officer.objects.filter(student_number=request.POST['temp_stn']).update(is_login=True, latest_login=time,
                                                                                   latest_logout=None)

    form = LoginForm
    return render(request, 'monitoring/login.html', {'form': form, 'officer_data': officer_data})


@login_required(login_url='admin:login')
def dreset(request):

    if request.method == "GET":
        Officer.objects.all().update(daily_time_spent=None,
                                     daily_time_spent_hour=None,
                                     daily_time_spent_minutes=None,
                                     is_login=False)

        return HttpResponse(200)


@login_required(login_url='admin:login')
def wreset(request):

    if request.method == "GET":
        Officer.objects.all().update(weekly_time_spent=None,
                                     weekly_time_spent_hour=None,
                                     weekly_time_spent_minutes=None,
                                     is_login=False)

        return HttpResponse(200)


@login_required(login_url='admin:login')
def history(request):
    pass


@login_required(login_url='admin:login')
def statistics(request):
    pass


@login_required(login_url='admin:login')
def profile(request):
    pass


@login_required(login_url='admin:login')
def reports(request):
    pass
