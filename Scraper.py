def scrape(link,format,pagestart,pagefin,):
	for i in range(pagestart, pagefin):	
		urllib.request.urlretrieve("{}{0:03d}{}".format(link,i,format))
		print("Downloading " + "{0:03d}".format(i))
