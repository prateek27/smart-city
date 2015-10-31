from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from login.models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.


def representative_analysis(request):
	user = request.user
	
	
	return render(request,"index.html",context_dict)


def representative_profile(request):
	user = request.user
	user_profile = UserProfile.objects.get(user=user)

	uPhoto = user_profile.profile_image.path
	
	substr = "/media/"
	position = uPhoto.find(substr)
	userimage = uPhoto[position:]

	context_dict = {'user':user,'userimage':userimage}
	return render(request,"user-profile-page.html",context_dict)

def representative_calender(request):
	user = request.user
	
	user_profile = UserProfile.objects.get(user=user)

	uPhoto = user_profile.profile_image.path
	
	substr = "/media/"
	position = uPhoto.find(substr)
	userimage = uPhoto[position:]


	
	context_dict = {'user':user,'userimage':userimage}
	
	return render(request,"calender.html",context_dict)


def representative_complaints(request):
	return HttpResponse("This is the complain section~!")


def representative_projects(request):
	return HttpResponse("This is the projects section !")


def representative_messages(request):
	return HttpResponse("This is the email section !")

def representative_quality_checks(request):
	context_dict={'user':request.user}
	return render(request,"index.html",context_dict)


def representative_contacts_view(request):
	context_dict={'user':request.user}
	return render(request,"contacts.html",context_dict)



@csrf_exempt
def save_message(request):
	user = request.user
	"""game_id=request.POST.get('game_id')
	game_score = request.POST.get('score')

	print(game_id)
	print(game_score)
	user = request.user
	print(user.id)	
	game = GameDetail.objects.get(id=game_id)
	print(game.game_name)
	submission = GameSubmission.objects.create(game=game,user=user,score=game_score)	
	"""
	return HttpResponse("Ok")

@csrf_exempt
def send_message(request):
	user = request.user

	to = request.POST.get('to')
	subject =request.POST.get('subject')
	message = request.POST.get('message')
	sender = user.first_name+" " + user.last_name

	new_subject =  sender + " shared a message on MySmartCity ! " + subject
	
	all_users = User.objects.all()
	for x in all_users:
		print(x.email)
		resp=send_mail(new_subject, message,sender,[x.email], fail_silently=True)	

	print(to)
	resp=send_mail(new_subject, message,sender,[to], fail_silently=True)
	print(resp)
	return HttpResponse("Ok")

