import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightning.jpg')
lightning_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(lightning_img, interpolation='none')

fig.show()

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'water.jpg')
water_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(water_img, interpolation='none')

fig.show()

lightning_img.paste(water_img, (730, 950), mask=water_img)
fig1, axes1 = plt.subplots(1, 1)
axes1[0].imshow(lightning_img, interpolation='none')
axes1[1].imshow(lightning_img, interpolation='none')
axes1[1].set_xlim(500, 1500)
axes1[1].set_ylim(1130, 850)
fig1.show()