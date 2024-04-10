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
from quotes.models import Quote, Author, Tag

json_path = Path(__file__).resolve().parent / 'quotes.json'

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:        
    author_instance, created = Author.objects.get_or_create(fullname=item['author'])
    
    quote = Quote(
        author=author_instance,
        quote=item['quote'],
        created_at=datetime.now()
    )
    quote.save()

    
    for tag_name in item['tags']:        
        tag_instance, created = Tag.objects.get_or_create(name=tag_name)
        quote.tags.add(tag_instance)
