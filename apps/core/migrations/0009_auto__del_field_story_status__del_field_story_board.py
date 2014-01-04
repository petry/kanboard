# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    depends_on = (
        ("core", "0008_migrate_to_boardposition"),
    )

    def forwards(self, orm):
        # Deleting field 'Story.status'
        db.delete_column(u'core_story', 'status_id')

        # Deleting field 'Story.board'
        db.delete_column(u'core_story', 'board_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Story.status'
        raise RuntimeError("Cannot reverse this migration. 'Story.status' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Story.status'
        db.add_column(u'core_story', 'status',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Step']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Story.board'
        raise RuntimeError("Cannot reverse this migration. 'Story.board' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Story.board'
        db.add_column(u'core_story', 'board',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Board']),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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