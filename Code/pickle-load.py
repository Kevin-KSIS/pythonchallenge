import urllib2, sys
import pickle

#getsource
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urllib2.urlopen(urllib2.Request(url)).read()
#write to file
file = open('banner.p','w')
file.write(text)
file.close()
#read from file and unpick
banner = pickle.load(open('banner.p','r'))

#
for i in banner:
	for j in i:
		sys.stdout.write(j[0]*j[1])
	print '\n'