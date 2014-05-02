# -*- encoding: utf-8 -*-

import logging

from django.core.management.base import BaseCommand, CommandError
from django_pancake.flatten import flatten, TemplateDirectories
import sys
import os
import codecs


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = "List of template directories and output base directory"
    help = "Flatten your templates into fluffy template pancakes."

    def make_pancakes(self, template_dirs, output_dir):
        templates = TemplateDirectories(template_dirs)
        for template_name in set(templates.list()):
            outfile = os.path.join(output_dir, template_name)
            print "'%s' -> '%s'" % (template_name, outfile)
            pancake = flatten(template_name, templates)
            try:
                os.makedirs(os.path.dirname(outfile))
            except OSError: # Already exists.
                pass
            with codecs.open(outfile, 'w', 'utf-8') as fp:
                fp.write(pancake)

    def handle(self, *args, **options):
        self.make_pancakes(args[1:-1], args[-1])
