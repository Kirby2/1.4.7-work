#DChambers_CHolloway 1.3.9
import Image 
import os 
import ImageMath
import matplotlib.pyplot as plt 

# Make sure python directory is in the folder where a rainforest.jpg, geometry.jpg, and fire.jpg can be found
#loads rainforest and geometric shapes
directory = os.path.dirname(os.path.abspath(__file__)) 
jungle_img = Image.open('rainforest.jpg')
jungle_img.load()
shapes_img = Image.open('geometry.jpg')
shapes_img.load()


# split images into rgb values
rjungle, gjungle, bjungle = jungle_img.split()
rshapes, gshapes, bshapes = shapes_img.split()


# mixes first edit
r = ImageMath.eval("int(a/((float(b)+1)/256))", a=rjungle, b=rshapes).convert('L')
g = ImageMath.eval("int(a/((float(b)+1)/256))", a=gjungle, b=gshapes).convert('L')
b = ImageMath.eval("int(a/((float(b)+1)/256))", a=bjungle, b=bshapes).convert('L')
#merges the values
imgOut = Image.merge("RGB", (r, g, b))
#saves the edit file
imgOut.save('firstedit.png', 'PNG')

#loads
fire_img = Image.open('fire.jpg')
fire_img.load()

fig, axes = plt.subplots(1, 3)
axes[1].imshow(fire_img, interpolation='none')
axes[2].imshow(jungle_img, interpolation='none')
axes[0].imshow(shapes_img, interpolation='none')
fig.show()

edit_img = Image.open('firstedit.png')
edit_img.load()
rfire, gfire, bfire = fire_img.split()
redit, gedit, bedit = edit_img.split()

#add fire image
r2 = ImageMath.eval("int(a/((float(b)+1)/256))", a=redit, b=rfire).convert('L')
g2 = ImageMath.eval("int(a*((float(b)+1)/256))", a=gedit, b=gfire).convert('L')
b2 = ImageMath.eval("int(a*((float(b)+1)/256))", a=bedit, b=bfire).convert('L')

imgOut = Image.merge("RGB", (r2, g2, b2))

imgOut.save('finaledit.png', 'PNG')

os.system('finaledit.png')