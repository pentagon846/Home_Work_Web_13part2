from django.shortcuts import render
from django.http import HttpResponse
from bson import ObjectId

from .utils import get_mongodb



def main(request, author_id):
    try:
        object_id = ObjectId(author_id)
        db = get_mongodb()
        author = db.authors.find_one({'_id': object_id})

        if author:
            return render(request, "authors/index.html", context={'authors': [author]})
        else:
            return HttpResponse(f"Author with ID {author_id} not found.")
    except Exception as e:
        return HttpResponse(f"Invalid author ID format: {e}")
    

