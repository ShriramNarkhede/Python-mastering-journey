import requests
import urllib.request as urllib2
import html2text
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/introduction-to-tensorflow/')

# check status code for response received
# success code - 200
print(r)

# print content of requ
#
# est
print(r.content)


soup = BeautifulSoup(urllib2.urlopen('http://example.com/page.html').read())

txt = soup.find('div', {'class' : 'body'})

print(html2text.html2text(txt))