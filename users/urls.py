'''url mapping for users related actions'''
from django.urls import path
from . import views

app_name = 'users' # pylint: disable=invalid-name
urlpatterns = [
    path('', views.sign_up, name='sign_up')
]
