import urllib.request
def scrape(link,format,pagestart,pagefin):
	for i in range(pagestart, pagefin):
		pagenumber = '{0:03d}'.format(i)
		url=("{}{}{}".format(link,pagenumber,format))
		urllib.request.urlretrieve(url,pagenumber+format)
		print("Downloading " + "{0:03d}".format(i) +" Out of " + str(pagefin))
