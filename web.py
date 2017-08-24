#!/usr/bin/python
import os
import sys
import urllib2
#import requests
import wget		#if import error ::: pip install wget
from bs4 import BeautifulSoup


def webscrap(url):
	print("Getting download link from page :",url)
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page,'html.parser')
	result= [element.text for element in soup.find("div", attrs={"class": "mirrorsa2"}).find_all('script')]
	i=str(result[0])
	test= i.splitlines()
	str1=test[7]
	start=test[7].find("http")
	end=test[7].find("?")
	return str1[start:end]


def generate_urls(start,end):
	print("Generarting urls to get download links......",start,end,type(end))
	url_base="http://animeheaven.eu/watch.php?a=One%20Piece%20Dubbed&e="
	fo=open("urls.txt","w")

	for i in range(start,end):
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
	
urls=[]
arguments=sys.argv
if (len(arguments) > 3):
	print("you need only two arguments download episodes from XXX to XXX....\n",len(arguments))
	print("try again...\n")
	sys.exit()
elif (len(arguments) < 3):
	print("you need only two arguments download episodes from XXX to XXX....\n",len(arguments))
        print("try again...\n")
        sys.exit()
else:
	print arguments[2]
	generate_urls(int(arguments[1]),int(arguments[2]))
	urls=get_urls_from_file()

	for i in range(0,len(urls)):
 		tryit=webscrap(urls[i])
		print(tryit)
		test_file = wget.download(tryit)
