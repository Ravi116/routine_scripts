#!/usr/bin/python
import os
import urllib2
import requests
import wget		#if import error ::: pip install wget
from bs4 import BeautifulSoup


#ecosmob = "http://animeheaven.eu/watch.php?a=One%20Piece%20Dubbed&e=526"

def webscrap(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page,'html.parser')
	result= [element.text for element in soup.find("div", attrs={"class": "mirrorsa2"}).find_all('script')]
	i=str(result[0])
	test= i.splitlines()
	str1=test[7]
	start=test[7].find("http")
	end=test[7].find("?")
	return str1[start:end]


def generate_urls():
	url_base="http://animeheaven.eu/watch.php?a=One%20Piece%20Dubbed&e="
	fo=open("urls.txt","w")

	for i in range(1,2):
	        print i
	        url=url_base+str(i)
	        print url
	        #fo.write('%s\n' % url)
	        fo.write(url)
	        fo.write('\n')
		fo.close()
	return

def get_urls_from_file():
	test = []
	fo=open("urls.txt","r")
	for line in fo:
        	test.append(line)
	return test
	
#ecosmob = "http://animeheaven.eu/watch.php?a=One%20Piece%20Dubbed&e=526"

urls=[]
generate_urls()
urls=get_urls_from_file()

for i in range(0,len(urls)):
 	tryit=webscrap(urls[i])
	print(tryit)
	#test_file = wget.download(tryit)

#print tryit
#r=requests.get(tryit)
#print len(r.content)
#urllib2.urlopen(tryit)
