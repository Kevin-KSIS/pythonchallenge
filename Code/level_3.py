import urllib2, re, sys

def request(url, data):
	r = urllib2.Request(url, data)
	res = urllib2.urlopen(r).read()
	return res

def enctext(text):
	m = text.index('<!--') + len('<!--')
	n = text.index('-->')
	return text[m:n]				

if __name__ == '__main__':
	url = 'http://www.pythonchallenge.com/pc/def/equality.html'
	source = request(url, '')
	data = enctext(source)
	print ''.join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))
	


