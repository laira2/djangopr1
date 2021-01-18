from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): 
    return HttpResponse("hello, world. you are at the polls index")

def detail(request, question_id):
    return HttpResponse("you are looking at question %s.", %question_id)
def vote(request, question_id):
    return HttpResponse("you are voiteing on question%s.", %question_id)
def results(request, question_id):
    return HttpResponse(response % question_id)

