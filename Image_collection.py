import cv2
import time
import os 
import uuid

#This is the path where our images are gonna saved 
IMAGES_PATH ='work-DIR/images/collectedimages'

#labels = ['hello' ,'thanks','yes','no','iloveyou']
labels = ['A' ,'B','C','D']


number_imgs = 5
path = 'work-DIR/images/collectedImages\\'

#this is the code which gonna save our images

for label in labels:
    os.mkdir(path+label)
    cap = cv2.VideoCapture(0)
    print('Collections images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret , frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname,frame)
        cv2.imshow("frame",frame)
        time.sleep(2)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()