
from django.shortcuts import render
from django.http import HttpResponse
from login.models import *
# Create your views here.


def citizen_view(request):
	user = request.user
	user_profile = UserProfile.objects.get(user=user)

	uPhoto = user_profile.profile_image.path
	
	substr = "/media/"
	position = uPhoto.find(substr)
	userimage = uPhoto[position:]

	context_dict = {'user':user,'userimage':userimage}
	return render(request,"user-citizen.html",context_dict)

def citizen_events(request):
	return HttpResponse("Citizen Profile")

