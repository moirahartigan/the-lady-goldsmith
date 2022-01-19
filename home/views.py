from django.shortcuts import render


def index(request):
    """ A View to return the index page """
    print("Tried to run")
    return render(request, 'home/index.html')
