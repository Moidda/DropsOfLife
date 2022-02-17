from django.shortcuts import render, get_object_or_404
from .models import User, Disease
from datetime import datetime

# Create your views here.


def index(request):
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

    context = {
        'user_disease': user_disease,
        'valid_donors': valid_donors
    }
    return render(request, 'user/index.html', context)
