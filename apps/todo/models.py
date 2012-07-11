
import datetime
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
    #creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.ForeignKey(Prio)
    user = models.ForeignKey(User)
    finished = models.BooleanField(default=False)

    def __unicode__(self):
        return self.subject
    
