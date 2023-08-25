# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import cv2 as cv

# load the image and convert it to a floating point data type
image = img_as_float(cv.imread("test.jpg"))

fig = plt.figure(figsize = (20, 30))
# loop over the number of segments
for it, i in ((2, 1), (5, 2), (15, 3)):
    numSegments = 16
    segments = slic(image, n_segments = numSegments, max_iter=it)

	# show the output of SLIC
    ax = fig.add_subplot(1, 3, i)
    ax.set_title("%d segments %d iter" % (numSegments,it))
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")

# show the plots
plt.show()


fig = plt.figure(figsize = (20, 30))
# loop over the number of segments
for numSegments, i in ((4, 1), (16, 2), (32, 3)):
    it = 15
    segments = slic(image, n_segments = numSegments, max_iter=it)

	# show the output of SLIC
    ax = fig.add_subplot(1, 3, i)
    ax.set_title("%d segments %d iter" % (numSegments,it))
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")

# show the plots
plt.show()

image = img_as_float(cv.imread("test2.jpg"))
fig = plt.figure(figsize = (20, 30))
for it, i in ((2, 1), (5, 2), (10, 3)):
    # loop over the number of segments
    numSegments = 1000
    segments = slic(image, n_segments = numSegments, max_iter=it)
    
    	# show the output of SLIC
    ax = fig.add_subplot(1, 3, i)
    ax.set_title("%d segments %d iter" % (numSegments,it))
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")

# show the plots
plt.show()