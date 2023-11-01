from django.urls import path
from . import views

app_name = 'housingapp'
urlpatterns = [
    path('', views.index, name='index')
    #path('applications', views.applications, name='applications'),
    #path('myapplications', views.myapplications, name='myapplications'),
    #path('application', views.application, name='application_create'),
    #path('application/<int:application_id>', views.application_existing, name='application_existing'),
]