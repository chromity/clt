from django.urls import path
from . import views

app_name = "monitoring"
urlpatterns = [
    path('', views.index, name="index"),
    path('history', views.history, name="history"),
    path('login', views.login, name="login"),
    path('statistics', views.statistics, name="statistics"),
    path('profile', views.profile, name="profile"),
    path('reports', views.reports, name="reports")
]