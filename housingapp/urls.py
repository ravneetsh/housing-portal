from django.urls import path
from . import views

app_name = 'housingapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('houseadvertisements', views.houseadvertisements, name='houseadvertisements'),
    path('myhouseadvertisements', views.myhouseadvertisements, name='myhouseadvertisements'),
    path('houseadvertisement', views.houseadvertisement, name='houseadvertisement_create'),
    path('houseadvertisement/<int:houseadvertisement_id>', views.houseadvertisement_existing, name='houseadvertisement_existing'),
    path('houseadvertisement/delete/<int:houseadvertisement_id>', views.houseadvertisement_delete, name='houseadvertisement_delete')
]