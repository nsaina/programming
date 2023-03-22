from skimage.io import imread, imshow, imsave
img =imread('tiger-low-contrast.png')
minim=img.min()
maxim=img.max()
print(maxim, minim)
img = (img - minim)*(255//(maxim - minim))
img.astype('uint8')