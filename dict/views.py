from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'dict/home.html')

def search(request):
    if request.method == 'POST':
        search_word = request.POST.get('search')
        word_meaning = requests.get('https://www.dictionary.com/browse/'+search_word)
        word_thesaurus = requests.get('https://www.thesaurus.com/browse/'+search_word)
    context = {
        'term': search_word
    }
    return render(request, 'dict/search.html', context)
