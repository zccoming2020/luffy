#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # django的环境配置也要加上dev
    # PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=day73_luffy.settings.dev
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day73_luffy.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    print("hello world!")
