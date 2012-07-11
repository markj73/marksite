# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prio'
        db.create_table('todo_prio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('todo', ['Prio'])

        # Adding model 'TodoItem'
        db.create_table('todo_todoitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.Prio'])),
        ))
        db.send_create_signal('todo', ['TodoItem'])


    def backwards(self, orm):
        # Deleting model 'Prio'
        db.delete_table('todo_prio')

        # Deleting model 'TodoItem'
        db.delete_table('todo_todoitem')


    models = {
        'todo.prio': {
            'Meta': {'object_name': 'Prio'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'todo.todoitem': {
            'Meta': {'object_name': 'TodoItem'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.Prio']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['todo']