from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageViem(request):
    return HttpResponse('hell project')
