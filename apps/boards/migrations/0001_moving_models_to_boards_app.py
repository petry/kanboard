# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('core_board', 'boards_board')
        db.rename_table('core_boardposition', 'boards_boardposition')
        db.rename_table('core_step', 'boards_step')
        db.rename_table('core_transition', 'boards_transition')

    def backwards(self, orm):
        db.rename_table('boards_board', 'core_board')
        db.rename_table('boards_boardposition', 'core_boardposition')
        db.rename_table('boards_step', 'core_step')
        db.rename_table('boards_transition', 'core_transition')

    models = {
        u'boards.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'boards.boardposition': {
            'Meta': {'object_name': 'BoardPosition'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boards.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['issues.Issue']", 'unique': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boards.Step']"})
        },
        u'boards.step': {
            'Meta': {'object_name': 'Step'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boards.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boards.Step']", 'null': 'True', 'blank': 'True'})
        },
        u'boards.transition': {
            'Meta': {'object_name': 'Transition'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['issues.Issue']"}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boards.Step']"})
        },
        u'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['boards']