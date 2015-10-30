from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length=200)
	event_date = models.DateTimeField(default = timezone.now())
	going = models.IntegerField(default=0)
	location = models.CharField(max_length=200)
	created_by = models.ForeignKey(User)

	def was_over(self):
		return self.event_date <= timezone.now() - datetime.timedelta(days=1)

	def __str__Event(self):
		return self.event_name


