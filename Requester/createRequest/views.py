from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    context = {}
    return render(request, "createRequest/index.html", context)


def processRequest(request):
    name = request.POST.get('fname')
    phone = request.POST.get('phone')
    address = request.POST.get('city')
    hospital_name = request.POST.get('hospital_name')
    prescription = request.FILES.get('prescription')
    fs = FileSystemStorage()
    filename = fs.save(prescription.name, prescription)
    uploaded_file_url = fs.url(filename)
    response = 'File Upload Successful. Go to this link: ' + uploaded_file_url
    return HttpResponse(response)
