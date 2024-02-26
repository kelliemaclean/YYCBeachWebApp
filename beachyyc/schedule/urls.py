from django.urls import path
from . import views
from .views import generate_schedule

urlpatterns = [
    path("", views.home, name="home"),
    path('generate-schedule/', generate_schedule, name='generate_schedule')
]

