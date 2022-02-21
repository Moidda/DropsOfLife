from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

import DropsOfLife.settings
from .models import Request


def index(request):
    context = {}
    return render(request, "forms-elements.html", context)


# After filling up create request form, this function is called for retrieving the
# form information for verification and creating new entry in the database
# Each request is stored in the Request table (see models.py)
def processRequest(request):
    name = request.POST.get('name')
    blood_type = request.POST.get('blood_type')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    hospital = request.POST.get('hospital')
    prescription = request.FILES.get('prescription')
    required_date = request.POST.get('required_date')
    required_time = request.POST.get('required_time')
    urgency = request.POST.get('gridRadios')

    response = name + ", " + blood_type + ", " + email + ", " + phone + ", " + address + ", " + hospital + ", " + urgency
    print(response)

    fs = FileSystemStorage()
    filename = fs.save(prescription.name, prescription)
    uploaded_file_url = fs.url(filename)
    response = 'File Upload Successful. Go to this link: ' + uploaded_file_url
    prescription_link = uploaded_file_url
    print(response)

    if not required_date:
        rqst = Request(
            name=name,
            phone=phone,
            address=address,
            hospital=hospital,
            blood_type=blood_type,
            urgency=urgency,
            prescription_link=prescription_link
        )
    else:
        rqst = Request(
            name=name,
            phone=phone,
            address=address,
            hospital=hospital,
            blood_type=blood_type,
            urgency=urgency,
            prescription_link=prescription_link,
            date=required_date
        )

    rqst.save()

    return render(request, "form-submitted.html", {'prescription': prescription_link})
