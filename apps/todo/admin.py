'''
Created on 9.7.2012

@author: Mark
'''
from apps.todo.models import *
from django.contrib import admin

admin.site.register(Prio)
admin.site.register(TodoItem)

