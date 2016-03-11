from PIL import Image, ImageDraw
import random
from math import sqrt

im=Image.new("RGB", (1024, 1024), "white")
draw=ImageDraw.Draw(im)
x=[]
y=[]
r=[]

for i in range(20):
	x.append(random.randrange(0,1024))
	y.append(random.randrange(0,1024))
	r.append(random.randrange(10,500))
	draw.ellipse((x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i]), fill=(255,255,0), outline='red')

counter1=0
for i in range(20):
	for j in range(20-i-1):
		d=sqrt((x[i+j+1] - x[i])**2 + (y[i+j+1] - y[i])**2)
		if r[i]+r[i+j+1]>=d:
			counter1+=1

print "Number of circles that intersect:", counter1			
im.show()