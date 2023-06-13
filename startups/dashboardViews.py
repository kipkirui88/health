from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from django.http import HttpResponseRedirect

from .models import Startups, Job
from .forms import StartupsForm, JobForm

# Create your views here.


def startup(request):
    context = {'startups': Startups.objects.all()}
    return render(request, 'dashboard.html', context)


