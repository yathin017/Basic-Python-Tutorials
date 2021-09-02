import cv2

img = cv2.imread('01_Read-Write-Show\lena.jpg',1)      # Reads coloured image
# img = cv2.imread('01_Read-Write-Show\lena.jpg',0)    # Reads grayscale mode 
# img = cv2.imread('01_Read-Write-Show\lena.jpg',-1)   # Reads Coloured image with alpha channels
print(img)

show_img = cv2.imshow('Image',img)

# cv2.waitKey(5000)                                    # holds image for 5 seconds before destroying

k = cv2.waitKey(0)
if k == 27:                                            # when Esc key is pressed the window closes
    cv2.destroyAllWindows()
elif k == ord('s'):                                    # when s is pressed the image is saved with the file name 'lena_copy.png'
    cv2.imwrite('lena_copy.png', img)
