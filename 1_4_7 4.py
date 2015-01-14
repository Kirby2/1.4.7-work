import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'storm.jpg')

storm_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(storm_img, interpolation='none')

axes[1].imshow(storm_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) 
axes[1].set_ylim(1100, 850)
fig.show()


water_file = os.path.join(directory, 'water.jpg')
water_img = PIL.Image.open(water_file)
water = water_img.resize((89, 87)) 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(water_img)
axes2[1].imshow(water)
fig2.show()

storm_img.paste(water, (730, 950), mask=water) 

fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(storm_img, interpolation='none')
axes3[1].imshow(storm_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.show()