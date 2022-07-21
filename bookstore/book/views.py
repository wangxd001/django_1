from django.shortcuts import render, HttpResponse


# Create your views here.
def shop(request, city, mobile):
    print(request.META)
    response = HttpResponse('OK')
    response['city'] = city
    response['mobile'] = mobile
    return response
    # pass
