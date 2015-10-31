from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
	project_name = models.CharField(max_length=200)
	project_date = models.DateTimeField(default = timezone.now())
	project_deadline = models.DateTimeField(default = timezone.now())
	current_spent = models.IntegerField(default=0)
	total_spent = models.CharField(max_length=200)
	started_by = models.ForeignKey(User)

	def was_over(self):
		return self.event_date <= timezone.now() - datetime.timedelta(days=1)

	def __str__Event(self):
		return self.event_name
