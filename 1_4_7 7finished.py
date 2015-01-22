#DChambers_CHolloway 1.3.9
import Image 
import os 
import ImageMath
import matplotlib.pyplot as plt 

# Make sure python directory is in the folder where a rainforest.jpg, geometry.jpg, and fire.jpg can be found
#loads rainforest and geometric shapes
directory = os.path.dirname(os.path.abspath(__file__)) 
jungle_img = Image.open('lightning.jpg')
jungle_img.load()
shapes_img = Image.open('water.jpg')
shapes_img.load()


# split images into rgb values
rjungle, gjungle, bjungle = jungle_img.split()
rshapes, gshapes, bshapes = shapes_img.split()


# mixes first edit
r = ImageMath.eval("int(a/((float(b)+1)/127))", a=rjungle, b=rshapes).convert('L')
g = ImageMath.eval("int(a/((float(b)+1)/127))", a=gjungle, b=gshapes).convert('L')
b = ImageMath.eval("int(a/((float(b)+1)/127))", a=bjungle, b=bshapes).convert('L')
#merges the values
imgOut = Image.merge("RGB", (r, g, b))
#saves the edit file
imgOut.save('firstedit.png', 'PNG')

#loads
fig, axes = plt.subplots(1, 2)

axes[1].imshow(jungle_img, interpolation='none')
axes[0].imshow(shapes_img, interpolation='none')
fig.show()


imgOut.save('finaledit.png', 'PNG')

os.system('finaledit.png')