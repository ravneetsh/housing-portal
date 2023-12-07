"""url mapping for housingapp"""
from django.urls import path
from . import views

app_name = 'housingapp' # pylint: disable=invalid-name
urlpatterns = [
    path('', views.index, name='index'),
    path('houseadvertisements',
            views.gethouseadvertisements,
            name='houseadvertisements'),
    path('myhouseadvertisements',
            views.myhouseadvertisements,
            name='myhouseadvertisements'),
    path('houseadvertisement',
            views.newhouseadvertisement,
            name='houseadvertisement_create'),
    path('houseadvertisement/<int:houseadvertisement_id>',
            views.houseadvertisement_existing,
            name='houseadvertisement_existing'),
    path('houseadvertisement/delete/<int:houseadvertisement_id>',
            views.houseadvertisement_delete,
            name='houseadvertisement_delete'),
    path('houseadvertisement/view/<int:houseadvertisement_id>',
            views.houseadvertisement_view,
            name='houseadvertisement_view')
]
