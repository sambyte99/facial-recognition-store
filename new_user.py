
import cv2
import os
import train
import time
 


def main ():
    from firebase import firebase
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
    user={}
    exists=[]
    #face_id = input('\n Enter user id end press <return> ==>  ')
    firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)
    result = firebase.get('pythondbtest-31f38/Customer', '')
    for y,z in result.items():
        exist= z["Cust_id"]
        exists.append(int(exist))
    print("Existing customer Ids are :", exists)
    for i in range(1, 10):
        if i not in exists:
            face_id=i
            break
    print("You have been assigned customer id :",face_id)
    print("Please remember it for further transactions")
    print("--------------------------------------------")
    time.sleep(6)

    ide=face_id
    name = input('Please give me your name :')
    phone= input('I would also like your phone number please:')

    print("\n Dont forget to smile while we take photos of your face :)")
# Initialize individual sampling face count
    count = 0

    while(True):

        ret, img = cam.read()
        #img = cv2.flip(img, -1) # flip video image vertically for the raspberry pi
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

        # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('Please keep shifting you face slowly', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100: # Take 100 face sample and stop video
             break

    # Do a bit of cleanup
    cam.release()
    cv2.destroyAllWindows()
    print("Yay! you are now a Customer for Raghavendra Stores! ")
    print("But wait!, Your balance is empty! Why dont you add some money? You can pay with just a smile :")
    print("1. Sure. I would love that.")
    print("2. Not now. I'll do it later, maybe..")
    amt=0
    ch=input("->")
    if ch=="1":
        print("Yay! Enter your bank details!")
        x=input("Enter card number:")
        x=input("Enter CVV:")
        #print("....Please assume you entered your bank details here....")
        print("Awesome! Now please enter the amount you ould like to start with:")
        amt=int(input("->Rs."))
        time.sleep(10)
        print("OTP sent! Confirm:")
        x=input("Enter Secret OTP:")
        print("Wait! While we speak with your bank......")
        time.sleep(10)
        print("Payment is sucessfull! You now have Rs.", amt, "in your account! Congratutulations! >v<")
    print("Okay! Thank you for your time and patience ! You can now use our store as a registered user!")
    user["Name"]=name
    user["Phone"]=phone
    user["Amount"]=amt
    user["Cust_id"]=str(ide)
    
    result = firebase.post('pythondbtest-31f38/Customer/',user)
    print(result)
    train.main()
    print("\nAlways remember! Your customer id is :",ide)

