from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from random import randrange
# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def random(request):
    
    if request.method == 'GET' and 'from' in request.GET:
        randomFrom = int(request.GET['from'])
    else:
        randomFrom = 0

    if request.method == 'GET' and 'to' in request.GET:
        randomTo =  int(request.GET['to'])
    else:
        randomTo = 100

    if randomFrom > randomTo or randomFrom == randomTo:
        res = { 'Error' : "the 'from' Num must be lower than the 'to' Num" }
    else:
        res = { 'answer' : randrange( randomFrom, randomTo ) }


    return JsonResponse(res)

