from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Home")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Hello there!!!! I'm here!!")
