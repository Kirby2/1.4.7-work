import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'water.jpg')
water_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(water_img, interpolation='none')

fig.show()