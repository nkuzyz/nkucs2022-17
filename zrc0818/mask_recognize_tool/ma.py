import cv2

from detect import mask

camera = cv2.VideoCapture(0)


while True:
    success, frame = camera.read()
    if not success:
        break
    else:
        cv2.imwrite('1.jpg', frame)
        frame=mask('1.jpg')
        cv2.imshow('1', frame)
        cv2.waitKey(1)