from django import template
from ..utils import get_mongodb

register = template.Library()

@register.filter(name='get_author_name')
def get_author_name(author_id):
    db = get_mongodb()
    author = db.authors.find_one({'_id': author_id})
    return author['fullname']

register.filter('author',get_author_name)