import cv2
from utils import get_limits
from PIL import Image

color = [0,255,255] #yellow
cap=cv2.VideoCapture(0)

while True:
    ret,frame= cap.read()

    hsvimage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color)

    mask = cv2.inRange(hsvimage,lowerlimit,upperlimit)

    mask_ = Image.fromarray(mask)

    bbox=mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2=bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
