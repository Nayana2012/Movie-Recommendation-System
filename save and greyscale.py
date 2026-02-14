import cv2
image = cv2.imread('example.jpg')
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_grey_image = cv2.resize(grey_image, (600, 400))
cv2.imshow('grey image', resized_grey_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grey_image.jpg', resized_grey_image)
    print("Grey image saved as 'grey_image.jpg'")
else:
    print("image not saved")
cv2.destroyAllWindows()
print(f"resized grey image dimension : {resized_grey_image.shape}")