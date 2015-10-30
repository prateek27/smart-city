from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	CITY_CHOICES = (('Chandigarh', 'Chandigarh'),('Jalandhar', 'Jalandhar'),('Amritsar','Amritsar'),('Ludhiana', 'Ludhiana'),)
	user = models.OneToOneField(User)
	#profile_handle = models.CharField(max_length = 200)
	user_city =  models.CharField(max_length=20, choices=CITY_CHOICES, default=CITY_CHOICES[0][0])
	profile_image = models.ImageField(upload_to="profile_image/",default="profile_image/default1.jpg",blank=True)

	def __str__(self):
		return self.user.username

class Leader(models.Model):
	user = models.OneToOneField(User)
	profile_image = models.ImageField(upload_to="profile_image/",default="profile_image/default1.jpg",blank=True)

	def __str__(self):
		return self.user.username

