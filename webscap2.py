# importing the library
from bs4 import BeautifulSoup
from urllib import request

# Initializing variable
url = "https://www.geeksforgeeks.org/matrix-introduction/"
gfg = BeautifulSoup(request.urlopen(url).read())

# Extracting data for article section
bodyHtml = gfg.find('article', {'class' : 'content'})

# Calculating result
res = bodyHtml.get_text() # type: ignore

# Printing the result
print(res)
