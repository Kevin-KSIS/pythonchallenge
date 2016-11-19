import sys, urllib2, re

if __name__ == '__main__':
	url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
	res = urllib2.urlopen(urllib2.Request(url)).read()
	l1 = res.index('@_')
	messg = res[l1:]
	for i in messg:
		if i.isalpha():
			sys.stdout.write(i)

#equality.html