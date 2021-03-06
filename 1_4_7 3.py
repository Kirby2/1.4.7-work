import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightning.png')

water_file = os.path.join(directory, 'water.png')
water_img = PIL.Image.open(water_file)
water = water_img.resize((960, 540)) 
fig1, axes1 = plt.subplots(1, 2)
axes1[0].imshow(water_img)
axes1[1].imshow(water_img)
fig1.show()

lightning_file = os.path.join(directory, 'lightning.png')
lightning_img = PIL.Image.open(lightning_file) 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(lightning_img)
axes2[1].imshow(lightning_img)
fig2.show()

result = PIL.Image.new('RGBA', lightning_img.size, (0,0,0,0))
result.paste(lightning_img, (0,0), mask=water)
fig3, axes3 = plt.sublots(1,2)
#axes3[0]. imshow(lightning_img, interpolation='none')
axes3[1]. imshow(result, interpolation='none')

fig3.show()