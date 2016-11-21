#connect the dots
import urllib2
from PIL import Image, ImageDraw

url = 'http://www.pythonchallenge.com/pc/return/good.html'
res = urllib2.urlopen(urllib2.Request(url, '', {'Authorization':'Basic aHVnZTpmaWxl'})).read()

# Get columns
l1 = res.index('first:') + len('first:')
l2 = res.index('second:')
X = [int(i) for i in res[l1:l2].replace('\n','').split(',')]

# Get rows
l3 = res.index('second:') + len('second:')


Y = [int(i) for i in res[l3:].replace('-->','').replace('\n','').split(',')]

# create a new picture
img = Image.new('RGB', (512, 512),'black')
img.save('image.png','png')

# draw
img = Image.open('image.png')
draw = ImageDraw.Draw(img)

draw.polygon(X, 'blue')
draw.polygon(Y, 'white')

img.show()
