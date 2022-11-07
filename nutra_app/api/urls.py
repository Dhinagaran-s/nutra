from django.urls import path
from . import views


app_name = 'aira_app'



urlpatterns = [
    path('register-api-user', views.register_api_user, name='register-api-user'),
]





