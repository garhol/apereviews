# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutText'
        db.create_table(u'about_abouttext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'about', ['AboutText'])


    def backwards(self, orm):
        # Deleting model 'AboutText'
        db.delete_table(u'about_abouttext')


    models = {
        u'about.abouttext': {
            'Meta': {'object_name': 'AboutText'},
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['about']