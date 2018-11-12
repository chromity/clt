from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
import logging

# enable logging in this application
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'monitoring/index.html')


def login(request):
    data = Officer.objects.order_by('-time_login')

    if request.method == "POST":
        pass
    else:
        form = LoginForm
        return render(request, 'monitoring/login.html', {'form': form, 'data': data})


def history(request):
    pass


def statistics(request):
    pass


def profile(request):
    pass


def reports(request):
    pass


