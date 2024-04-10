import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")

import django
django.setup()

from django.core.management import call_command

import json
from datetime import datetime
from django.utils.dateparse import parse_datetime
from quotes.models import Author

json_path = Path(__file__).resolve().parent / 'authors.json'

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:    
    author = Author(
        fullname=item['fullname'],
        born_date=item['date_born'],
        born_location=item['location_born'],
        description=item['bio'],
        created_at=datetime.now(),
    )
    author.save()
    
