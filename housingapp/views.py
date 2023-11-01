from django.shortcuts import render
from django.http import HttpResponse
from .models import HouseAdvertisement
from .forms import HouseAdvertisementForm
from django.contrib import messages
from django.http import Http404

# Create your views here.
def index(request):
    context = {}
    return render(request, 'housingapp/index.html', context)
    
def houseadvertisement(request):
    # Get emtry form , create it, get an existing houseadvertisement, update it
    if request.method == 'GET':
        form = HouseAdvertisementForm()
    else:
        form = HouseAdvertisementForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'House Advertisement saved successfully. House Advertisement Id is ' + str(instance.id))
            return render(request, 'users/messages.html',{})
        else:
            print('House AdvertisementForm has errors')
    context = {"form": form}    
    return render(request, 'housingapp/houseadvertisement.html', context)
    
def houseadvertisement_existing(request, houseadvertisement_id):
    if request.method == 'GET':
        try:
            houseadvertisement = HouseAdvertisement.objects.get(pk=houseadvertisement_id)
            form = HouseAdvertisementForm(instance=houseadvertisement)
        except HouseAdvertisement.DoesNotExist:
            raise Http404("House Advertisement does not exist")
        context = {'form': form, 'id': houseadvertisement_id}
        return render(request, 'housingapp/houseadvertisement.html', context)
    else:
        rs = HouseAdvertisement.objects.get(id=houseadvertisement_id)
        form = HouseAdvertisementForm(request.POST, instance=rs)
        if form.is_valid():
            form.save()
            messages.success(request, 'House Advertisement updated successfully')
            context = {'form': form, 'id': houseadvertisement_id}
            return render(request, 'housingapp/houseadvertisement.html', context)
            
# Get list of all houseadvertisements
def houseadvertisements(request):
    houseadvertisements = HouseAdvertisement.objects.order_by('-id')[:]
    context = {'houseadvertisements': houseadvertisements}
    return render(request, 'housingapp/houseadvertisements.html', context)
    
def myhouseadvertisements(request):
    houseadvertisements = HouseAdvertisement.objects.filter(user=request.user).order_by('-id')[:]
    context = {'houseadvertisements': houseadvertisements, "are_my_houseadvertisements": True}
    return render(request, 'housingapp/houseadvertisements.html', context)