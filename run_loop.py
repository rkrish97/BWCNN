 #pip3 install matplotlib
#sudo apt install python3-opencv

import cv2
import time
def textx(image,ttt,x,y):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    # org 
    org = (x,y) 
    # fontScale 
    fontScale = 0.5
    # Blue color in BGR 
    color = (0, 255, 0) 
    # Line thickness of 2 px 
    thickness = 1
    # Using cv2.putText() method 
    image = cv2.putText(image, ttt , org, font, fontScale, color, thickness, cv2.LINE_AA) 

cap = cv2.VideoCapture(0)


# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
i=0
k=0
ttt=time.time()
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)
        height, width, channels = frame.shape

    #frame.CAP_PROP_FRAME_COUNT CV_CAP_PROP_FRAME_COUNT
    #print( cv2.CAP_PROP_FPS)

    #################### Face ##########################
    x1=int(width*0.35)
    y1=int(height*0.10)

    x2=int(width*0.65)
    y2=int(height*0.90)

    #cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    cropped = frame[y1:y2, x1:x2]
    #################### Left ##########################
    x1=int(width*0.35)+10
    y1=int(height*0.30)

    x2=int(width*0.50)-5
    y2=int(height*0.50)

    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    textx(frame,"Left Eye",x1+5,y1-5)
    #cropped_l = frame[y1+1:y2-1, x1+1:x2]
    #cropped_l = cv2.cvtColor(cropped_l, cv2.COLOR_BGR2GRAY)
    #################### Right ##########################
    x1=int(width*0.50)+5
    y1=int(height*0.30)
    x2=int(width*0.65)-10
    y2=int(height*0.50)
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    textx(frame,"Right Eye",x1+5,y1-5)
    cropped_r = frame[y1+1:y2-1, x1+1:x2]
    cropped_r = cv2.cvtColor(cropped_r, cv2.COLOR_BGR2GRAY)
    ##############################################
    croppedx = cropped[50:150,0:1000]
    #cv2.imshow("cropped", cropped)
    cv2.imshow('Input', croppedx)
    
    c = cv2.waitKey(1)

    if c==-1:  # normally -1 returned,so don't print it
        if k==1:
            #print("Save")
            #cv2.imwrite("frame.jpg", cropped)
            ##cv2.imwrite("pic/{:05d}frame_l.jpg".format(i), cropped_l)
            nnn=time.time()
            iiii="{0}".format(nnn-ttt)#str(round(nnn-ttt,2))
            sss="pic/{:05d}_"+iiii+"_frame_r.jpg"
            print (time.asctime( time.localtime() ))
            cv2.imwrite(sss.format(i), cropped_r)

            #sss="pic/{:05d}_"+str(round(nnn-ttt,2))+"_frame_l.jpg"
            #cv2.imwrite(sss.format(i), cropped_l)
            # sleep=0.1 -> fps=7
            # 0.2 -> 4 fps
            # 0.3 -> 3 fps
            # 0.4 -> 2 fps
            time.sleep(0.1)#065)
            ttt=nnn
            i=i+1
            continue
    elif c == 32:
            if k==0:
                k=1
                print("Record")
            else:
                k=0
                print("Stop")
    elif c == 27:
            break

cap.release()
cv2.destroyAllWindows()
