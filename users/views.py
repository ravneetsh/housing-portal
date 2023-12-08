'''user related views'''
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm

# Create your views here.
@require_http_methods(["GET", "POST"]) #NOSONAR
def sign_up(request):
    '''view for signup of user'''
    if request.method == "POST":
        print('POST')
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                f'Account has been successfully created for {username}!')
            return redirect('sign_in')
        print('Form not valid')
        print(form.error_messages)
    if request.method == "GET":
        print('GET')
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
    