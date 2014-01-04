# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BoardPosition'
        db.create_table(u'core_boardposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Story'], unique=True)),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Board'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Step'])),
        ))
        db.send_create_signal(u'core', ['BoardPosition'])


    def backwards(self, orm):
        # Deleting model 'BoardPosition'
        db.delete_table(u'core_boardposition')


    models = {
        u'core.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.boardposition': {
            'Meta': {'object_name': 'BoardPosition'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"}),
            'story': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Story']", 'unique': 'True'})
        },
        u'core.step': {
            'Meta': {'object_name': 'Step'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']", 'null': 'True', 'blank': 'True'})
        },
        u'core.story': {
            'Meta': {'object_name': 'Story'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"})
        },
        u'core.transition': {
            'Meta': {'object_name': 'Transition'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Story']"})
        }
    }

    complete_apps = ['core']