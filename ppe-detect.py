from ultralytics import YOLO
import cv2
import cvzone
import math

#cap = cv2.VideoCapture(0)   #for webcam
#cap.set(3, 1280)
#cap.set(4, 720)

cap = cv2.VideoCapture("../videos/cons6.mp4")

model = YOLO("../Yolo-weights/bestppe.pt")
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person',
              'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

while True:
    success, img = cap.read()
    #img = cv2.resize(img, [1280, 720], interpolation=cv2.INTER_AREA)
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            w, h = x2-x1, y2-y1

            # confidence
            conf = math.ceil(box.conf[0]*100)/100
            # classes
            cls = int(box.cls[0])
            # display
            if conf>0.5:
                if classNames[cls] in ('NO-Hardhat', 'NO-Mask', 'NO-Safety Vest'):
                    mycolor= [0, 0, 255]
                elif classNames[cls] in ('Hardhat', 'Mask','Safety Cone', 'Safety Vest'):
                    mycolor= [0, 255, 0]
                else:
                    mycolor= [255, 0, 0]
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, t=3, rt=2, colorR=(205, 205, 0), colorC=mycolor)
                # cv2.rectangle(img, [x1, y1 - 10], [x2, y2], color=mycolor)
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', [max(0, x1), max(35, y1 - 10)],
                                   scale=0.4, thickness=1, offset=3, colorR=mycolor, colorT=(0, 0, 0))
    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 27:  # close on ESC key
        break
cap.release()
cv2.destroyAllWindows()