import new_user
from firebase import firebase
import time

print("---------------------------------------------------------------------\n                     Welcome to Raghavendra Stores!\n---------------------------------------------------------------------\n")
print("\n\ņ\nYou are accessing Admin features here\nBe responsible as if your marks depends on it.\nBecause it does.\n\n") 
print("How may I help you?\n1.Add new user\n2.Add money to existing user\n3.Check account Balance and other details\n4.Delete a user\n5.Exit")
ch=input("->")
if (ch=="1"):
	new_user.main()
if (ch=="2"):
	ide=input("Enter you customer ID:")
	firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)
	result = firebase.get('pythondbtest-31f38/Customer', '')
	found=0
	for y,z in result.items():
		#print('ID:',y)
	#print('Items:',z)
		if z["Cust_id"]==ide:
			print("User found!\n\n---------------------------")
			found=1
			break
	if(found==0):
		print("OOPS. Seems like no one exists with that customer ID. Sorry! Gonna have to ask you to recheck your details")
		exit()
	for i,j in z.items():
		print(i,j)
	uniq=y
	damt=z["Amount"]
	print("------------------------------------\n\n")
	amt=int(input("Enter the amount you wish to add:  Rs."))
	print("Yay! Enter your bank details!")
	x=input("Enter card number:")
	x=input("Enter CVV:")
       		#print("....Please assume you entered your bank details here....")
	time.sleep(5)
	print("OTP sent! Confirm:")
	x=input("Enter Secret OTP:")
	print("Wait! While we speak with your bank......")
	time.sleep(5) 
	amt=amt+damt
	firebase.put('pythondbtest-31f38/Customer/'+str(uniq),'Amount',amt)
	print('YAY! Process successful! ')
	print("Current Amount : Rs.",amt)
if ch=="3":
	ide=input("Enter you customer ID:")
	found=0
	firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)
	result = firebase.get('pythondbtest-31f38/Customer', '')
	for y,z in result.items():
		#print('ID:',y)
	#print('Items:',z)
		if z["Cust_id"]==ide:
			found=1
			print("User found!\n\n---------------------------")
			break
	if (found==0):
		print("OOPS. Seems like no one exists with that customer ID. Sorry! Gonna have to ask you to recheck your details")
		exit()
	for i,j in z.items():
		print(i,j)
	print("------------------------------------\n\n")
if ch=="4":
	ide=input("Enter you customer ID:")
	found=0
	firebase = firebase.FirebaseApplication('https://pythondbtest-31f38.firebaseio.com/', None)
	result = firebase.get('pythondbtest-31f38/Customer', '')
	for y,z in result.items():
		#print('ID:',y)
	#print('Items:',z)
		if z["Cust_id"]==ide:
			print("User found!\n\n---------------------------")
			found=1
			break
	if (found==0):
		print("OOPS. Seems like no one exists with that customer ID. Sorry! Gonna have to ask you to recheck your details")
		exit()
	for i,j in z.items():
		print(i,j)
	uniq=y
	print("------------------------------------\n\n")
	print("Are you really really sure you want to remove ",z["Name"],"forever and ever?")
	really=input("Y (DO IT!!!) / N (I changed my mind):--->")
	if really=='Y':
		firebase.delete('/pythondbtest-31f38/Customer/', uniq)
		print('Record Deleted')
	else:
		print("Okay! We won't be deleting then.")

		