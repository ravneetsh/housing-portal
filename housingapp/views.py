'''views defined for advertisements'''
from django.views.decorators.http import require_GET, require_http_methods
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from .models import HouseAdvertisement, City
from .forms import HouseAdvertisementForm

HOUSE_ADVERTISEMENT_TEMPLATE = 'housingapp/houseadvertisement.html'

# Create your views here.
@require_GET
def index(request):
    '''home page for application'''
    context = {}
    return render(request, 'housingapp/index.html', context)

@require_http_methods(["GET", "POST"]) #NOSONAR
def newhouseadvertisement(request):
    '''view method for getting a blank form and a filled one saved'''
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
    return render(request, HOUSE_ADVERTISEMENT_TEMPLATE, context)

@require_http_methods(["GET", "POST"]) #NOSONAR
def houseadvertisement_existing(request, houseadvertisement_id):
    '''view method for getting form for an existing advertisement and then saving its update'''
    if request.method == 'GET':
        try:
            houseadvertisement = HouseAdvertisement.objects.get(pk=houseadvertisement_id) # pylint: disable=no-member
            form = HouseAdvertisementForm(instance=houseadvertisement)
        except HouseAdvertisement.DoesNotExist as e: # pylint: disable=no-member
            raise Http404("House Advertisement does not exist") from e
        context = {'form': form, 'id': houseadvertisement_id}
        return render(request, HOUSE_ADVERTISEMENT_TEMPLATE, context)

    result = HouseAdvertisement.objects.get(id=houseadvertisement_id) # pylint: disable=no-member
    form = HouseAdvertisementForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        messages.success(request, 'House Advertisement updated successfully')
    context = {'form': form, 'id': houseadvertisement_id}
    return render(request, HOUSE_ADVERTISEMENT_TEMPLATE, context)

# Get list of all houseadvertisements
@require_GET
def gethouseadvertisements(request):
    '''getting list of all advetisements'''
    cities = City.objects.order_by('name')[:] # pylint: disable=no-member
    city_id=request.GET.get('city_id','0')
    if city_id == '0':
        houseadvertisements = HouseAdvertisement.objects.filter( # pylint: disable=no-member
                advertisement_visibility=1
            ).order_by('-id')[:]
    else:
        houseadvertisements = HouseAdvertisement.objects.filter( # pylint: disable=no-member
                advertisement_visibility=1, city__pk=int(city_id)
            ).order_by('-id')[:]
    context = {
        'houseadvertisements': houseadvertisements,
        'cities': cities,
        'city_id': [int(city_id)]  
    }
    return render(request, 'housingapp/houseadvertisements.html', context)

@require_GET
def myhouseadvertisements(request):
    '''getting list of my advertisements'''
    cities = City.objects.order_by('name')[:] # pylint: disable=no-member
    city_id=request.GET.get('city_id','0')
    if city_id == '0':
        houseadvertisements = (
            HouseAdvertisement.objects.filter(user=request.user) # pylint: disable=no-member
            .order_by('-id')[:]
            )
    else:
        houseadvertisements = HouseAdvertisement.objects.filter( # pylint: disable=no-member
                user=request.user, city__pk=int(city_id)
            ).order_by('-id')[:]

    context = {
        'houseadvertisements': houseadvertisements, 
        "are_my_houseadvertisements": True,
        'cities': cities,
        'city_id': [int(city_id)]
    }
    return render(request, 'housingapp/houseadvertisements.html', context)

@require_GET
def houseadvertisement_delete(request, houseadvertisement_id):
    '''deleting an advertisement'''
    messages.success(request, 'House Advertisement Id - '
        + str(houseadvertisement_id) + ' deleted successfully.')
    HouseAdvertisement.objects.filter(id=houseadvertisement_id).delete() # pylint: disable=no-member
    return render(request, 'housingapp/messages.html', {})

@require_GET
def houseadvertisement_view(request, houseadvertisement_id):
    '''getting data of an advertisement for view'''
    try:
        houseadvertisement = HouseAdvertisement.objects.get(pk=houseadvertisement_id) # pylint: disable=no-member
        form = HouseAdvertisementForm(instance=houseadvertisement)
    except HouseAdvertisement.DoesNotExist as e: # pylint: disable=no-member
        raise Http404("House Advertisement does not exist") from e
    context = {'form': form, 'id': houseadvertisement_id, 'view': True}
    return render(request, HOUSE_ADVERTISEMENT_TEMPLATE, context)
