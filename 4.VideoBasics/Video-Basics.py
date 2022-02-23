
## Connecting to Camera

import cv2

capture = cv2.VideoCapture(0)

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

# writer = cv2.VideoWriter('video.mp4v', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))


while True:
    
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # writer.write(gray)
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
#writer.release()
cv2.destroyAllWindows()








## Using Video Files

import time

cap = cv2.VideoCapture('../images/video.mov')


if cap.isOpened() == False: 
    print("Error! File no found.")

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        
        # 20 fps
        #time.sleep(1/20)  
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    else:
        break
        
        
cap.release()
cv2.destroyAllWindows()


