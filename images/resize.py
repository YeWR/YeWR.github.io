import cv2

img = cv2.imread('fig.jpg')

height, width = 512, 512
dst = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)

cv2.imwrite('fig.png', dst)
cv2.waitKey(0)
