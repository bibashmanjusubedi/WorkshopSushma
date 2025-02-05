# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r'rajeshdai.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'rajeshsir'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

image = cv2.imread(path,0) #grayscale read
cv2.imshow("b&w",image)
cv2.waitKey()

# closing all open windows
cv2.destroyAllWindows()