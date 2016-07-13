from tifffile import imread
import matplotlib.pyplot as plt

filename = "Ni300K.tif"
array = imread(filename)

print(array.shape)

plt.imshow(array)
plt.show()
