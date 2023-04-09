#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import urllib
import bs4


# In[3]:


# found

url = "https://wuzzuf.net/search/jobs/?q=python&a=hpb"

# not found
#url = "http://abcxyz.com/"

try:
    page = urllib.request.urlopen(url).read().decode('utf-8')
except urllib.error.HTTPError as e:
    print("HTTP error")
except urllib.error.URLError as e:
    print("URL error")
else:
    print(page)


# In[4]:


url = "https://en.wikipedia.org/robots.txt"

source = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(source, 'lxml')
soup


# Write a Python program to display the name of the most recently added dataset on data.gov.
# 

# In[6]:


url = "https://catalog.data.gov/dataset?q=&sort=metadata_created+desc"

source = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(source, 'lxml')

h3_heading = soup.find('h3')

fetch_recent = h3_heading.find('a').contents
fetch_recent


# Q. Write a Python program to extract h1 tag from example.com
# 

# In[7]:


url = "http://example.com/"

source = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(source, 'lxml')

print(soup.h1)


# Write a Python program to extract and display all the header tags

# In[8]:


url = "https://en.wikipedia.org/wiki/Main_Page"

page = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(page, 'lxml')

headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

all_headers = soup.findAll(headers)

["".join(str(header)) for header in all_headers]


# Write a Python program to extract and display all the image links 

# In[9]:


import re

url = "https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)"

source = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(source, 'lxml')

all_images = soup.findAll('img', attrs = {'src': re.compile('.jpg')})

[image['src'] for image in all_images]


# Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page.

# In[11]:


url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

page = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(page, 'lxml')

[link.get('href') for link in soup.findAll('a')]


# Write a Python program to check whether a page contains a title or not.
# 

# In[13]:


def check_title(url):
    
    page = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(page, 'lxml')
    if soup.title:
        print("Title Present")
        return soup.title
    else:
        print("None")
        return False
    
check_title("http://example.com/")


# Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org

# In[14]:


url = "https://www.wikipedia.org/"

source = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(source, 'lxml')

lang = soup.findAll('div', attrs = {'class': 'central-featured-lang'})
#print(lang)

[print(l.getText()) for l in lang]


# Write a Python program to get the number of people visiting a U.S. government website right now

# In[15]:


import requests

page = requests.get("https://analytics.usa.gov/data/live/realtime.json")

print(page.json()['data'])


# Write a Python program to download IMDB's Top 250 data (movie name, Initial release, director name and stars).

# In[24]:


url = "https://www.imdb.com/chart/top"
page = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(page, 'lxml')

movie_list = soup.select('td.titleColumn')
movie_rating_list = soup.select('td.imdbRating')

for i in range(0, len(movie_list)):
    movie_title = movie_list[i].find('a').text.strip()
    movie_year = movie_list[i].find('span').text.strip()
    movie_stars = movie_list[i].find('a').get('title')
    movie_rating = movie_rating_list[i].find('strong').text.strip()
    print(i + 1, ")", movie_title, movie_year, ",", "Starring: ", movie_stars, ",", "Rating: ", movie_rating)


# In[ ]:




