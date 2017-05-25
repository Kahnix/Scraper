#!/usr/bin/env python3
#Getting modules we need
import os
from os import system
import urllib.request
#Dumb pretty work
x = input("Press enter to begin")
print("Pulling your book down for you")
#The range here would be the page numbers you want, if the url has book-40,book-41...
for i in range(x,y):
	#Converts 10 = 010
	pagenumber='{0:03d}'.format(i)
	#Selects format eg jpg
	format = ".jpg"
	#Entering the URL for scraping
	url = '' + pagenumber + format
	#Retrieving each page (dwonloading it)
	urllib.request.urlretrieve(url, pagenumber + format)
	print("Downloading " + pagenumber)
print("Compressing now...")
#Compress file down to 200 Kilobytes.
os.system("jpegoptim --size=200k *.jpg")
#Turn file into a pdf
pdf = input ("Done! Would you like me to turn this file into a PDF document? Y/N ").lower()
if pdf == "y":
	name = input("What would you like me to name it?")
	os.system("convert `ls -v *.jpg`" + name)
else:
	exit
