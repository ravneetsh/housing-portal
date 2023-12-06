'''views defined for advertisements'''
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from .models import HouseAdvertisement, City
from .forms import HouseAdvertisementForm

# Create your views here.
def index(request):
    '''home page for application'''
    context = {}
    return render(request, 'housingapp/index.html', context)

def newhouseadvertisement(request):
    '''view method for getting a black form and a filled one saved'''
    # Get entry form , create it, get an existing houseadvertisement, update it
    if request.method == 'GET':
        form = HouseAdvertisementForm()
    else:
        form = HouseAdvertisementForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'House Advertisement saved successfully.\
                House Advertisement Id is ' + str(instance.id))
            return render(request, 'users/messages.html',{})
        print('House AdvertisementForm has errors')

    context = {"form": form}
    return render(request, 'housingapp/houseadvertisement.html', context)

def houseadvertisement_existing(request, houseadvertisement_id):
    '''view method for getting form for an existing advertisement and then saving its update'''
    if request.method == 'GET':
        try:
            houseadvertisement = HouseAdvertisement.objects.get(pk=houseadvertisement_id)
            form = HouseAdvertisementForm(instance=houseadvertisement)
        except HouseAdvertisement.DoesNotExist:
            raise Http404("House Advertisement does not exist")
        context = {'form': form, 'id': houseadvertisement_id}
        return render(request, 'housingapp/houseadvertisement.html', context)

    result = HouseAdvertisement.objects.get(id=houseadvertisement_id)
    form = HouseAdvertisementForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        messages.success(request, 'House Advertisement updated successfully')
    context = {'form': form, 'id': houseadvertisement_id}
    return render(request, 'housingapp/houseadvertisement.html', context)

# Get list of all houseadvertisements
def gethouseadvertisements(request):
    '''getting list of all advetisements'''
    cities = City.objects.order_by('name')[:]
    city_id=request.GET.get('city_id','0')
    if city_id == '0':
        houseadvertisements = HouseAdvertisement.objects.filter(
                advertisement_visibility=1
            ).order_by('-id')[:]
    else:
        houseadvertisements = HouseAdvertisement.objects.filter(
                advertisement_visibility=1, city__pk=int(city_id)
            ).order_by('-id')[:]
    context = {
        'houseadvertisements': houseadvertisements,
        'cities': cities,
        'city_id': [int(city_id)]  
    }
    return render(request, 'housingapp/houseadvertisements.html', context)

def myhouseadvertisements(request):
    '''getting list of my advertisements'''
    cities = City.objects.order_by('name')[:]
    city_id=request.GET.get('city_id','0')
    if city_id == '0':
        houseadvertisements = (
            HouseAdvertisement.objects.filter(user=request.user)
            .order_by('-id')[:]
            )
    else:
        houseadvertisements = HouseAdvertisement.objects.filter(
                user=request.user, city__pk=int(city_id)
            ).order_by('-id')[:]

    context = {
        'houseadvertisements': houseadvertisements, 
        "are_my_houseadvertisements": True,
        'cities': cities,
        'city_id': [int(city_id)]
    }
    return render(request, 'housingapp/houseadvertisements.html', context)

def houseadvertisement_delete(request, houseadvertisement_id):
    '''deleting an advertisement'''
    messages.success(request, 'House Advertisement Id - '
        + str(houseadvertisement_id) + ' deleted successfully.')
    HouseAdvertisement.objects.filter(id=houseadvertisement_id).delete()
    return render(request, 'housingapp/messages.html', {})

def houseadvertisement_view(request, houseadvertisement_id):
    '''getting data of an advertisement for view'''
    try:
        houseadvertisement = HouseAdvertisement.objects.get(pk=houseadvertisement_id)
        form = HouseAdvertisementForm(instance=houseadvertisement)
    except HouseAdvertisement.DoesNotExist:
        raise Http404("House Advertisement does not exist")
    context = {'form': form, 'id': houseadvertisement_id, 'view': True}
    return render(request, 'housingapp/houseadvertisement.html', context)
