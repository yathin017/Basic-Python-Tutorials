import cv2

cap = cv2.VideoCapture(0);

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # Associated number = 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Associated number = 4 

cap.set(3, 1208)    # setting width
cap.set(4, 720)     # setting height

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()