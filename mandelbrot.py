'''
Sarah Yildirim
11/4/20
OMH
Sources: The links and dropbox pdf that was provided.
Description: For my project, I decided to draw two mandelbrot fractals and one julia set. For the mandelbrot set, I used
the code we did in class, and changed it around and played around with the numbers and iterations. For the julia set, I 
copied over the same code and made c a constant in order to get the julia set. I really enjoyed this project a lot and would
definitely recommend this project again. This was very fun and I enjoyed playing around with the numbers in order to get
different patterns. Overall, my favorite picture is the second one because I really like the dark black, grey, white fade
I used. For the Julia set, I really liked the background with the black and white and the black oval.
'''


#the first mandelbrot fractal
from PIL import Image

# defining the mandelbrot function
def mandelbrot(c, z=complex(0,0), count=0):
	z = z**2+c
	count += 3
	if abs(z) >= 4 or count > maxIteration:
		return count
	return mandelbrot(c, z, count)

#max iterations
maxIteration = 255

#image area
xmin = -0.34444331275720164
xmax = -0.29976147976680384
ymin = -0.6490672410836762
ymax = -0.6043854080932783

#image size
imgx, imgy = 1000, 1000

image = Image.new("RGB",(imgx, imgy))

#assigning each pixel a place on the complex plane
for y in range(imgy):
	cy = y * (ymax-ymin)/(imgy-2) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin)/(imgx-1) + xmin
		c = complex(cx,cy)
		iterations = mandelbrot(c)
		#coloring the drawing
		r = (iterations*20)%256
		g = (iterations*20)%256
		b = (iterations*5)%256
		image.putpixel((x,y), (r,g,b))


#saving and printing the drawing
image.save("mandelbrotone_picture.png","PNG")



#the second mandelbrot fractal

#image area
xmin = 0.24547322591145
xmax = 0.3036549886067
ymin = -0.031829833984
ymax = 0.0263519287109


#assigns each pixel a place on the complex plane
for y in range(imgy):
	cy = y * (ymax-ymin)/(imgy) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin)/(imgx-5) + xmin
		c = complex(cx,cy)
		iterations = mandelbrot(c)
		#this determines the colors (red, green, blue components)
		if iterations >= 10:
			r = (iterations*2)%90
			g = (iterations*2)%90
			b = (iterations*2)%90
		else:
			r = 114
			g = 129
			b = 228
		image.putpixel((x,y), (r,g,b))


#saving and printing the drawing
image.save("mandelbrottwo_picture.png","PNG")



#the julia fractal

#defining the julia function

#image area
xmin = -2
xmax = 2
ymin = -2
ymax = 2

#assigning pixel values on the complex plane
for y in range(imgy):
	zy = y * (ymax-ymin)/(imgy-2) + ymin
	for x in range(imgx):
		zx = x * (xmax-xmin)/(imgx-1) + xmin
		z = complex(zx,zy)
		iterations = mandelbrot(complex(0.2806738476953905, 0.010095190380761565),z)
		
		#coloring according to the iterations (background for the oval)
		if iterations >= 2:
			r = (iterations*2)%230
			g = (iterations*5)%230
			b = (iterations*3)%230
		else:
			r = 255
			g = 255
			b = 255

		image.putpixel((x,y), (r,g,b))

#printing the julia set
image.save("juliaset_picture.png","PNG")

'''
Comments/Feedback:

Grace Liu: I think you should add a background to the back of your julia set so that it can pop.
	Resolved by adding an oval behind the drawing and making the background more interesting.

Michael: Change the color scheme of your second mandelbrot. The color scheme seems too similar to the first mandelbrot.
	Resolved by changing the color scheme of the second mandelbrot to something darker and making it look like it's fading.

My Mom: The zoom of the first mandelbrot doesn't seem very interesting. Maybe change the zoom to something that has more going on.
	Resolved by changing the zoom of the mandelbrot to something that has more going on.

'''
