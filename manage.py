#!/usr/bin/env python
import imp
import sys
import os

# assume 'apps' is a directory with same parent directory as us
APPS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'root', 'apps'))
#FOO = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)
#    sys.path.insert(0, FOO)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
