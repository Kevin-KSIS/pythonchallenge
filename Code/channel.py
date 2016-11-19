import pickle, re, zipfile, sys

#read file readme.txt -> hint1: start from 90052
file = zipfile.ZipFile('channel.zip')
nextfile = "90052"

while True:
	try:
		sys.stdout.write(file.getinfo(nextfile+'.txt').comment)
		f = file.read(nextfile+'.txt')
		nextfile = ''.join(re.findall("\d", f))			
	except:
		break

# oxygen

