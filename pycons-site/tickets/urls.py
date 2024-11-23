from django.urls import path
from . import views

app_name = 'tickets'
urlpatterns = [
    path('', view=views.ticket, name='ticket'),
    path('register', view=views.register, name='register'),
]
