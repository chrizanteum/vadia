# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usb'
        db.create_table('motherboard_usb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('motherboard', ['Usb'])

        # Adding model 'Socket'
        db.create_table('motherboard_socket', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('socket', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('motherboard', ['Socket'])

        # Adding model 'Motherboard'
        db.create_table('motherboard_motherboard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ram', self.gf('django.db.models.fields.IntegerField')()),
            ('connectors_number', self.gf('django.db.models.fields.IntegerField')()),
            ('usb', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['motherboard.Usb'], unique=True)),
        ))
        db.send_create_signal('motherboard', ['Motherboard'])

        # Adding M2M table for field socket on 'Motherboard'
        db.create_table('motherboard_motherboard_socket', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('motherboard', models.ForeignKey(orm['motherboard.motherboard'], null=False)),
            ('socket', models.ForeignKey(orm['motherboard.socket'], null=False))
        ))
        db.create_unique('motherboard_motherboard_socket', ['motherboard_id', 'socket_id'])


    def backwards(self, orm):
        # Deleting model 'Usb'
        db.delete_table('motherboard_usb')

        # Deleting model 'Socket'
        db.delete_table('motherboard_socket')

        # Deleting model 'Motherboard'
        db.delete_table('motherboard_motherboard')

        # Removing M2M table for field socket on 'Motherboard'
        db.delete_table('motherboard_motherboard_socket')


    models = {
        'motherboard.motherboard': {
            'Meta': {'object_name': 'Motherboard'},
            'connectors_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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