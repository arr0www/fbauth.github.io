from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def facebook_login_view (request):
    return render(request, 'home.html')


@login_required
def profile (request):
    return render(request, 'profile.html')

