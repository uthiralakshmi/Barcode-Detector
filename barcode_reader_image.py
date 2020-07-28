# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2
import numpy as np
import os
import glob
#import skimage.exposure

# traverse the folder containing images

root_dir="/home/uthira/Documents/OpenCV/Complete barcode scanner for images and videos/images/input/"
for filename in os.listdir(root_dir):     
	print(filename)	
        # load the input image
	dire= os.path.join(root_dir,filename)
	image = cv2.imread(dire)
	# find the barcodes in the image and decode each of the barcodes
	barcodes = pyzbar.decode(image)
	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw the
		# bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it on
		# our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)
		head=filename.split(',')
		name = head[0]+'_output.jpg'
		output_dir=os.path.join("/home/uthira/Documents/OpenCV/Complete barcode scanner for images and videos/images/output/",name)
	print(name)
	cv2.imwrite(output_dir, image)
	cv2.waitKey(0)

