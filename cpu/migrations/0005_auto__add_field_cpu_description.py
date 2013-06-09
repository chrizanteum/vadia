# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cpu.description'
        db.add_column('cpu_cpu', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cpu.description'
        db.delete_column('cpu_cpu', 'description')


    models = {
        'cpu.cpu': {
            'Meta': {'object_name': 'Cpu'},
            'cores': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'frequency': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'socket': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['motherboard.Socket']", 'null': 'True'})
        },
        'motherboard.socket': {
            'Meta': {'object_name': 'Socket'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socket': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['cpu']