'''
Created on 10.7.2012

@author: Mark
'''
from django import forms

from apps.todo.models import *


class TodoItemForm(forms.ModelForm):
    """
    Form for creating a new Todo item.
    """
    
    class Meta:
        model = TodoItem
        exclude = ('user', 'creation_date')

    def save(self, user, *args, **kwargs):
        commit = kwargs.get('commit', True)
        kwargs['commit'] = False

        item = super(TodoItemForm, self).save(*args, **kwargs)
        item.user = user
        
        if commit:
            item.save()

        return item