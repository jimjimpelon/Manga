from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . import models
from django.utils import timezone

BASE_MANGKAKALOT_URL = 'https://mangakakalot.com/search/story/{}'



def home(request):
    response = requests.get('https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page=1')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('div', {'class':'list-truyen-item-wrap'})


    final_posting_home = []

    for post in post_titles:
        title = post.find('a').get('title')
        url = post.find('a').get('href')
        images = post.find('a').find('img').get('src')
        views = post.find('div').find('span').text

        final_posting_home.append((title, url, images, views))

    context = {
        'final_posting_home' : final_posting_home
    }
    return render(request, 'base.html', context)



def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search, created=timezone.now())
    search_connector = '_'.join(search.split())
    final_url= BASE_MANGKAKALOT_URL.format(search_connector)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('div', {'class':'story_item'})


    final_postings = []

    for post in post_titles:
        title = post.find('h3').text
        title_url = post.find('h3').find('a').get('href')
        image_url = post.find('a').find('img').get('src')
        views = post.text.split('\n')
        final_views = ""
        final_author = ""
        for i in views:
            if 'View' in i:
                final_views += i
            elif 'Author(s)' in i:
                final_author += i

        final_postings.append((title, title_url, image_url,final_author,final_views))


    context = {
        'search' : search,
        'final_postings' : final_postings,
    }
    return render(request, 'my_app/new_search.html', context)

def category(request):
    response = requests.get('https://mangakakalot.com/manga_list?type=topview&category=30&state=all&page=1')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('ul',{'class':'tag tag-name'})
    


    return render(request, 'my_app/category.html')