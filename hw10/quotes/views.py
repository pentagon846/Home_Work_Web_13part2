from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
from .forms import QuoteForm, AuthorForm, TagForm
from .models import Quote, Author  
from django.contrib.auth.decorators import login_required #new 7/3

def main(request, page=1):
    per_page = 10
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, per_page)
    quote_on_page = paginator.page(page)

    author_ids = set(quote.author.id for quote in quote_on_page.object_list)
    
    authors = Author.objects.filter(id__in=author_ids)
    author_dict = {str(author.id): author for author in authors}
    
    for quote in quote_on_page.object_list:
        author_id = str(quote.author.id)
        quote.author_object = author_dict.get(author_id, {})

    return render(request, 'quotes/index.html', context={'quotes': quote_on_page, 'authors': authors})

@login_required
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('quotes:root')
    else:
        author_form = AuthorForm()

    return render(request, 'quotes/add_author.html', context={'author_form': author_form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            return redirect('quotes:root')
    else:
        quote_form = QuoteForm()

    return render(request, 'quotes/add_quote.html', context={'quote_form': quote_form})

@login_required
def author_details(request, author_id):    
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/authors.html', context={'author': author}) #index_id