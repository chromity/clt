from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from .forms import *
import logging

# enable logging in this application
logger = logging.getLogger(__name__)


@login_required(login_url='admin:login')
def index(request):
    return render(request, 'monitoring/index.html')


@login_required(login_url='admin:login')
def login(request):
    officer_data = Officer.objects.order_by('-daily_time_spent')

    if request.method == "POST":
        officer_obj = get_object_or_404(Officer, student_number=request.POST['temp_stn'])

        if officer_obj.is_login:
            login_obj = get_object_or_404(Login, time_login=officer_obj.latest_login)
            time = datetime.now(timezone.utc)

            duration = time - login_obj.time_login

            if time.isocalendar()[1] != datetime.now().isocalendar()[1]:
                weekly_time_spent = duration

                weekly_time_spent_hours = weekly_time_spent.total_seconds() // 3600
                weekly_time_spent_minutes = (weekly_time_spent.total_seconds() % 3600) // 60
            else:
                weekly_time_spent = officer_obj.weekly_time_spent + duration

                weekly_time_spent_hours = weekly_time_spent.total_seconds() // 3600
                weekly_time_spent_minutes = (weekly_time_spent.total_seconds() % 3600) // 60

            if time.strftime("%A") != datetime.now().strftime("%A"):
                daily_time_spent = duration

                daily_time_spent_hours = daily_time_spent.total_seconds() // 3600
                daily_time_spent_minutes = (daily_time_spent.total_seconds() % 3600) // 60
            else:
                daily_time_spent = officer_obj.daily_time_spent + duration

                daily_time_spent_hours = daily_time_spent.total_seconds() // 3600
                daily_time_spent_minutes = (daily_time_spent.total_seconds() % 3600) // 60

            Officer.objects.filter(student_number=request.POST['temp_stn'])\
                           .update(weekly_time_spent=weekly_time_spent,
                                   daily_time_spent=daily_time_spent,
                                   latest_logout=time,
                                   is_login=False,
                                   weekly_time_spent_hour=weekly_time_spent_hours,
                                   weekly_time_spent_minutes=weekly_time_spent_minutes,
                                   daily_time_spent_hour=daily_time_spent_hours,
                                   daily_time_spent_minutes=daily_time_spent_minutes)
            Login.objects.filter(time_login=officer_obj.latest_login).update(time_logout=time, duration=duration)
        else:
            form = LoginForm(request.POST)
            event_login = form.save(commit=False)
            event_login.officer = officer_obj  # save officer from queried student number
            time = datetime.now()  # save time user login
            event_login.time_login = time
            event_login.temp_stn = request.POST['temp_stn']
            event_login.save()

            Officer.objects.filter(student_number=request.POST['temp_stn']).update(is_login=True, latest_login=time, latest_logout=None)

        form = LoginForm
        return render(request, 'monitoring/login.html', {'form': form, 'officer_data': officer_data})
    else:
        form = LoginForm
        return render(request, 'monitoring/login.html', {'form': form, 'officer_data': officer_data})


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
