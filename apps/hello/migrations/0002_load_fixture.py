# -*- coding: utf-8 -*-
from django.core.management import call_command
from south.v2 import DataMigration

from utils.fixture import southern_models


class Migration(DataMigration):
    def forwards(self, orm):
        with southern_models(orm):
            call_command("loaddata", "my_fixture.json")
