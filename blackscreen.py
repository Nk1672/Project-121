import cv2
import time
import numpy as np

op = cv2.VideoWriter_fourcc(*'XVID')
op_file = cv2.VideoWriter('output.avi', op, 20.0, (640, 480))
cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg,axis = 1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img,axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerBlack = np.array([0,120,50])
    upperBlack = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lowerBlack, upperBlack)

    lowerBlack = np.array([170,120,70])
    upperBlack = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lowerBlack, upperBlack)
    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3),np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3),np.uint8))

    mask2 = cv2.bitwise_not(mask1)
    reset1 = cv2.bitwise_and(img, img, mask=mask1)
    reset2 = cv2.bitwise_and(bg, bg, mask=mask2)
    final_output = cv2.addWeighted(reset1, 1, reset2, 0, 0)
    
    op_file.write(final_output)
    cv2.imshow("Project C121", final_output)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destrpyAllWindows()
