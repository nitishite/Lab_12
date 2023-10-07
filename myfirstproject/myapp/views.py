from django.shortcuts import render
from django.http import HttpResponse

#creating my views here
def hi(request):
    return render(request, 'myapp/home.html')
