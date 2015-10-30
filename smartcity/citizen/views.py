
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def citizen_view(request):
	return HttpResponse("Hello Citizen !")