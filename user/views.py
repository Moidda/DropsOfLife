from django.shortcuts import render, get_object_or_404, redirect

import DropsOfLife.settings
from .models import User, Disease
from datetime import datetime

# Create your views here.


def index(request):
    context = {}

    user_disease = []
    valid_donors = []
    diseases = Disease.objects.all()
    for d in diseases:
        users = User.objects.filter(diseases__name=d.name)
        for u in users:
            user_disease.append({'name': u.name, 'disease': d.name})
            print(u.name + " " + d.name)

    donors = User.objects.all()
    for d in donors:
        delta = datetime.now().date() - d.dateOfBirth
        if delta.days > 40 and d.isDonor:
            valid_donors.append({'name': d.name})

    context['user_disease'] = user_disease
    context['valid_donors'] = valid_donors

    return render(request, 'user/index.html', context)
