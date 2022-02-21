from django.shortcuts import render, HttpResponse

from Requester.createRequest.models import Request


# def myrev(item):
#     revitem = []
#     for i in item:
#         revitem.append(i)
#
#     return revitem.reverse()


def index(request):
    request_immediate = Request.objects.all().filter(urgency='Immediate').order_by('-date').reverse()
    request_standby = Request.objects.all().filter(urgency='Stand By').order_by('-date').reverse()
    request_longterm = Request.objects.all().filter(urgency='Long Term').order_by('-date').reverse()

    # request_standby = myrev(request_standby)

    context = {
        'request_immediate': request_immediate,
        'request_standby': request_standby,
        'request_longterm': request_longterm
    }
    return render(request, "DropsOfLifeHomepage.html", context)
