from skimage import data, exposure, img_as_float, color,io
from matplotlib import pyplot as plt
images = io.imread_collection('18.png')
counter = 0;
directory = ''
for img in images:
    img = exposure.equalize_hist(img)
    str1 = directory + str(counter) + '.png'
    print(str1)
    io.imsave(str1, img)
    str1 = ''
    counter += 1
