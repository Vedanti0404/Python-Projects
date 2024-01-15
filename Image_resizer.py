# Import the OpenCV library
import cv2

# Specify the source image file name
source = "image.jpg"

# Specify the destination image file name
destination = 'newImage.png'

# Set the scale percentage for resizing
scale_percent = 50

# Read the image from the source file
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Calculate the new width and height based on the scale percent
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize the image using the calculated width and height
output = cv2.resize(src, (new_width, new_height))

# Write the resized image to the destination file
cv2.imwrite(destination, output)
