import numpy as np
import cv2

# img = cv2.imread('03_Geometric-Shapes\lena.jpg', 1)             # Normal Image
img = np.zeros([512,512,3], np.uint8)                           # Image creation using numpy zeros  


# img = cv2.line(img, (0,0), (255,255), (0,255,0), 2)           # filename, starting point, ending point, color(RGB), thickness
# img = cv2.arrowedLine(img, (0,0), (255,255), (0,255,0), 2)    # filename, starting point, ending point, color, thickness
# img = cv2.rectangle(img, (0,0), (255,255), (0,255,0), 2)      # filename, starting point(diagonal), ending point(diagonal), color, thickness
# img = cv2.rectangle(img, (0,0), (255,255), (0,255,0), -1)     # filename, starting point, ending point, color, thickness(if thickness is in negative it fills the shape)
img = cv2.circle(img, (255,255), 63, (0,255,0), 2)              # filename, center, radius, color, thickness

font = cv2.FONT_HERSHEY_COMPLEX                                 # font type
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,0), 10, cv2.LINE_AA)   # filename, text, position, font type, color, thickness, line type


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()