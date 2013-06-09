# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Motherboard.price'
        db.add_column('motherboard_motherboard', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Motherboard.price'
        db.delete_column('motherboard_motherboard', 'price')


    models = {
        'motherboard.motherboard': {
            'Meta': {'object_name': 'Motherboard'},
            'connectors_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ram': ('django.db.models.fields.IntegerField', [], {}),
            'socket': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['motherboard.Socket']", 'symmetrical': 'False'}),
            'usb': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['motherboard.Usb']", 'unique': 'True'})
        },
        'motherboard.socket': {
            'Meta': {'object_name': 'Socket'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socket': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'motherboard.usb': {
            'Meta': {'object_name': 'Usb'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['motherboard']