import cv2
import time

cam = cv2.VideoCapture(0)
cv2.namedWindow("Taking Photos")
img_counter = 0
while (img_counter<5):
    ret, frame = cam.read()
    cv2.imshow("Taking Photos", frame)
    k = cv2.waitKey(1)
    img_name = "Image_{}.png".format(img_counter)
    # frame = cv2.resize(frame, (224,224))
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(img_name, frame)
    print("{} saved!".format(img_name))
    img_counter += 1
    time.sleep(3)    
        
cam.release()
cv2.destroyAllWindows()
