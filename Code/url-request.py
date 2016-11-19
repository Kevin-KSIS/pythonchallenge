import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
i = '12345'
while True:
	response = urllib2.urlopen(urllib2.Request(url%i)).read()
	print response
	#
	if 'html' in response:
		exit(0)
	#
	try:
		idx = response.index('nothing is ') + len('nothing is ')
		i = response[idx:]
	except:
		i = str(int(i)/2)
#peak.html
	