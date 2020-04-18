import cv2
import numpy as np
import os 
from firebase import firebase
def main():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
    id = 0

# names related to ids: example ==> Sambit: id=1,  etc
    names = []
    names.append('None')
    result = firebase.get('pythondbtest-31f38/Customer', '')
    for y,z in result.items():
        names.append(str(z["Name"]))
    #print("Names are :")
    #print(names)
    names.append("unknown")
    names.append("unknown")
    names.append("unknown")



# Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically in case you using da pi cam

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
	    
	

        # Check if confidence is less than 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                if ((100-confidence)>50):
                    #print(str(id)) remove the hash to debug
                    cam.release()
                    cv2.destroyAllWindows()
                    return(str(id))
                confidence = "  {0}%".format(round(100 - confidence))
	    
	    
            else:
                id = 'unknown'
                cam.release()
                cv2.destroyAllWindows()
                return(str(id))
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
            cv2.imshow('Please wait, while we admire your face',img) 

      

# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    

