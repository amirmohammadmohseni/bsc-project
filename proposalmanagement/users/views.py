from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
