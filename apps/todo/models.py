
import datetime
import pytz

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prio(models.Model):
    code = models.CharField(max_length=20)
    value = models.IntegerField()

    def __unicode__(self):
        return self.code

class TodoItem(models.Model):
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    creation_date = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.ForeignKey(Prio)
    user = models.ForeignKey(User)
    finished = models.BooleanField(default=False)
    estimate = models.IntegerField(verbose_name='Estimated time in hours', default=0)
    
    def score(self):
        now = datetime.datetime.now(pytz.utc)
        hours_left = (self.deadline - now).days * 8
        if (hours_left == 0):
            hours_left = 1
        return 1000*self.priority.value*self.estimate/hours_left  
        
        
    def __unicode__(self):
        return self.subject
    
