from django.shortcuts import render, HttpResponse


# Create your views here.
def shop(request, city, mobile):
    print(request.META)
    response = HttpResponse('OK')
    response['city'] = city
    response['mobile'] = mobile
    return response


def set_session(request, name):
    u_id = 1
    request.session['u_id'] = u_id
    request.session['username'] = name
    return HttpResponse('Set session success.')
