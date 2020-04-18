import face
import qr
import re
import datetime
from firebase import firebase
uk=0
print("\n---------------------------------------------------------------------\n     Welcome to Raghavendra Stores\n---------------------------------------------------------------------\n")
print("")
print("Currently we have these for sale!")
print("Potatoes at Rs 10")
print("Tomatoes at Rs 20")
print("Onions at Rs 30")
print("")
print("Please show us your beautiful face:")
name=face.main()
if name=='unknown' or name=="unknown":
    uk=1
if uk==0:
    print("Hey ! I know you ! You are :", name)
else:
    print("Sorry ! I guess we have never met before stranger!")
entry = datetime.datetime.now()
print("You entered the shop at ",entry)
item=""
total=0
items=[]
bill = {
    "Name":name,
    "Entry_time": entry,
  "Potato": 0,
  "Tomato": 0,
  "Onion": 0,
  "Total": 0,
  "Exit_time" :entry,
}
invert=1
while True:
    print("Scan QR:")
    item=qr.main()
    rem=0
    if item=="done" or item=="Done" or item=="DONE":
        print("Inputs Done!")
        break
    if item=="invert":
        if invert==1:
            print("You have changed to Remove mode!\n Scan a QR to remove it!")
            invert=-1
        else:
            print("You are already in remove mode! No! You can't remove the remove function")
            invert=-1
    if item=="add":
        if invert==-1:
            print("You have reverted back to add mode!\nScan QR to add items")
            invert=1
        else:
            print("You are already in add mode. No need to show off. Jeez.")
            invert=1
  
    if item in items and invert==-1:
        items.remove(item)
    if item in items and item!="add" and item!="invert":
        print("Item already exists!")
    else:
        if item not in items and item!="invert" and item!="add" and invert==1:
            items.append(item)
        blep=""
        x = re.search("^Potato.*$", item)
        if (x):
            if invert==1:
                bill["Potato"] = bill.get("Potato")+1
                blep="Potato"
                total=total+10
            if invert==-1:
                print("Potato currently:",bill["Potato"])
                if bill.get("Potato")>0:
                    blep="Potato"
                    bill["Potato"] = bill.get("Potato")-1
                    total=total-10
                    rem=1
                else:
                    print("Dude! You dont have any more Potatoes to remove!")
                    rem=0
        x = re.search("^Tomato.*$", item)
        if (x):
            if invert==1:
                bill["Tomato"] = bill.get("Tomato")+1
                blep="Tomato"
                total=total+20
            if invert==-1:
                print("Tomato currently:",bill["Tomato"])
                if bill.get("Tomato")>0:
                    blep="Tomato"
                    bill["Tomato"] = bill.get("Tomato")-1
                    total=total-20
                    rem=1
                else:
                    print("Dude! You dont have any more Tomatoes to remove!")
                    rem=0
        x = re.search("^Onion.*$", item)
        if (x):
            if invert==1:
                
                bill["Onion"] = bill.get("Onion")+1
                blep="Onion"
                total=total+30
            else:
                print("Onion currently:",bill["Onion"])
                if bill.get("Onion")>0:
                    blep="Onion"
                    bill["Onion"] = bill.get("Onion")-1
                    total=total-30
                    rem=1
                else:
                    print("Dude! You dont have any more Onions to remove!")
                    rem=0
        if item != "add" and item != "invert":
            if invert==1:
                print("New item:",blep)
            if invert==-1 and rem==1:
                print("Removed item:",blep)
            if invert==-1 and rem==0:
                print("Cant remove what wasnt added")
exsit = datetime.datetime.now()
print("You exited the shop at ",exsit)
bill["Exit_time"] = exsit
print("")
print("") 
print("Your bill will be generated. Please wait!")
print("Hope to see you again",name,"! :)")
print("")
print("") 
print("         Raghavendra Stores PVT LTD")

bill["Total"] = total
for y,z in bill.items():
    print(y,"  -  ",z) 

firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)
result = firebase.post('pythondbtest-31f38/Bill/',bill)
print(result)
if uk==1:
    print("Stranger! Kindly Pay the amounnt of Rs.",total, "at the counter!")
    exit()
result = firebase.get('pythondbtest-31f38/Customer', '')
for y,z in result.items():
    if z["Name"]==name:
        print("User found!\n\n---------------------------")
        for i,j in z.items():
            print(i,j)
        uniq=y
        damt=z["Amount"]
        amt=damt-total
        if(amt<0):
            amt=-amt
            print("Oh no! looks like you do not have that much money! Please pay the remaining Rs.",amt," in cash to our cashier")
            amt=0
        else:
            print("Amount Decuced from your account : Rs.",total)
        firebase.put('pythondbtest-31f38/Customer/'+str(uniq),'Amount',amt)
        print('Record Updated')
        print("Current Amount : Rs.",amt)

