from PIL import Image
import sys

# get size
img = Image.open('oxygen.png')
img.load()
X, Y = img.size

# get pixel
text = ''
for x in range(0,X-21,7):
	main_px = img.getpixel((x,48))
	sys.stdout.write(chr(main_px[0]))
	text += chr(main_px[0])

# get flag
flag = text[text.index('[')+1:-1]
flag = [int(i) for i in flag.split(', ')]
print '\n',flag
for i in flag:
	sys.stdout.write(chr(i))

#integrity

