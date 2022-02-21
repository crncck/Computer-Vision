import cv2 

img = cv2.imread('../images/dog.jpg')

while True:
    
    cv2.imshow('Dog', img)
    
    # If waited for at least 1 millisecond and pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()