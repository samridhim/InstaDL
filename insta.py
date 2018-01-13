from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
ss = raw_input("Enter url")
filename = raw_input("Enter file name without extension")
print ss
s=ss.rsplit('/',1)
soup = bs(urlopen(s[0]))
print soup
parsed = list(urlparse.urlparse(s[0])) 
print parsed
image = soup.find("meta", property = "og:image")
if image:
	url = image["content"]
	[filename, headers] = urlretrieve(url,filename + ".jpg") 
	print filename
	print headers
else:
	print "no image given"
