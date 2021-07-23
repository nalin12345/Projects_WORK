import cv2

img=cv2.imread(r'C:\Courses\Internship\nalin.jpeg')
 
# Prints Dimensions of the image
print(img.shape)
resized_image = cv2.resize(img,(500,1000))

cv2.imwrite("new.png",resized_image)
cv2.imshow('kuchbhi',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



