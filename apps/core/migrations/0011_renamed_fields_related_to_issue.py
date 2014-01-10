# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('core_boardposition', 'story_id', 'issue_id')
        db.rename_column('core_transition', 'story_id', 'issue_id')

    def backwards(self, orm):
        db.rename_column('core_boardposition', 'issue_id', 'story_id')
        db.rename_column('core_transition', 'issue_id', 'story_id')

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
            'issue': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Issue']", 'unique': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"})
        },
        u'core.issue': {
            'Meta': {'object_name': 'Issue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.step': {
            'Meta': {'object_name': 'Step'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']", 'null': 'True', 'blank': 'True'})
        },
        u'core.transition': {
            'Meta': {'object_name': 'Transition'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Issue']"}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"})
        }
    }

    complete_apps = ['core']