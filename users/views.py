from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.models import User, Group

# Create your views here.
def sign_up(request):
    print('HHHHHHHHHHHH')
    if request.method == "POST":
        print('POST')
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(request,
                'Account has been successfully created for {}!'.format(un))
            return redirect('sign_in')
        else:
            print('Form not valid')
            print(form.error_messages)
    if request.method == "GET":
        print('GET')
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
    