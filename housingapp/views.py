from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'housingapp/index.html', context)