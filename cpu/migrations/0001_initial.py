# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cpu'
        db.create_table('cpu_cpu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('socket', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['motherboard.Socket'], null=True)),
        ))
        db.send_create_signal('cpu', ['Cpu'])


    def backwards(self, orm):
        # Deleting model 'Cpu'
        db.delete_table('cpu_cpu')


    models = {
        'cpu.cpu': {
            'Meta': {'object_name': 'Cpu'},
            'frequency': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'socket': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['motherboard.Socket']", 'null': 'True'})
        },
        'motherboard.socket': {
            'Meta': {'object_name': 'Socket'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socket': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['cpu']