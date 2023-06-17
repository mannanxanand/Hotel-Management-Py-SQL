# Hotel Management System By Mannan Anand (11620057)

import sys
import csv
import time


print('\t---------------------------')
print('\t YUMA HOTELS AND RESORTS')
print('\t---------------------------')
time.sleep(2)
print()
print('\t-----------------------------------------')
print('\t WELCOME TO YUMA HOTEL MANAGEMENT SYSTEM')
print('\t-----------------------------------------')


# Define global variables
Hotel_fields = ['ID', 'Name', 'Age','Address','Country', 'Email', 'Mobile','Checkin date','Checkout date','Room number','Roomrent','Restaurent bill','Laundry bill','Gaming bill','Total bill']
Hotel_database = 'Hotelrecord.csv'


###################################################################################
def add_Customer():
   print("-------------------------")
   print("Add Customer Information")
   print("-------------------------")
   global Hotel_fields
   global Hotel_database


   Customer_data = []
   for i in range(9):
       value = input("Enter " + Hotel_fields[i] + ": ")
       Customer_data.append(value)



   print ("\n ***** We have The Following Rooms For You *****")
   print (" 1. Studio -----> Rs.10000")
   print (" 2. Elite -----> Rs.5000 ")
   
   print (" 3. Double -----> Rs.3500 ")
   print (" 4. Single -----> Rs.2500  \n")


   roomchoice=int(input("Enter Your Choice Please->"))
   noofdays=int(input("Number of nights :"))
   roomno=int(input("Enter Customer Room No : "))
   Customer_data.append(roomno)


   if roomchoice==1:
      roomrent = noofdays * 10000
      print("\nStudio Room Rent : ",roomrent)
   elif roomchoice==2:
      roomrent = noofdays * 5000
      print("\nElite Room Rent : ",roomrent)
   elif roomchoice==3:
      roomrent = noofdays * 3500
      print("\nDouble Room Rent : ",roomrent)
   elif roomchoice==4:
      roomrent = noofdays * 2500
      print("\nSingle Room Rent : ",roomrent)
   else:
      print("Invalid Input, Please Try Again !!! ")
      return


   dt=[0,0,0,roomrent]
   Customer_data.append(roomrent)
   Customer_data=Customer_data+dt


   with open(Hotel_database, "a", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerows([Customer_data])

   print("\nData saved successfully")
   print(input("\nPress any key to continue"))
   return

###########################################################


def restaurentbill():
   ID=int(input("Enter your ID:"))
   print("\n*****RESTAURANT MENU*****\n")
   print("""1.water----->Rs.10 \n2.tea----->Rs15 \n3.breakfast combo-->Rs1150 \n4.lunch---->Rs900 \n5.dinner--->Rs1200 \n6.Exit\n""")

   choice=int(input("Enter your choice:"))
   quantity=int(input("Enter the quantity:"))

   if (choice==1):
      rtbill = quantity * 10
   elif (choice==2):
      rtbill = quantity * 15
   elif (choice==3):
      rtbill = quantity * 1150
   elif (choice==4):
      rtbill = quantity * 900
   elif (choice==5):
      rtbill = quantity * 1200
   elif (choice==6):
      return
   else:
      print("Invalid option")
      return

   print ("Total Food Cost=Rs",rtbill,"\n")

   with open(Hotel_database, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      data =[]
      for i in reader:
         if len(i) > 1:
            if i[0] == str(ID):
               i[11] = eval(i[11]) + rtbill
               i[14] = eval(i[14]) + rtbill
               data.append(i)
            else:
               data.append(i)
   with open(Hotel_database, "w", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerows(data)

   print(input('\nPress any key to continue'))
   return

########################################################### 
def gamingbill():
   ID=int(input("Enter your ID:"))
   print ("\n******GAMING MENU*******\n")
   print("""1. Table Tennis -----> 150 Rs./HOURS \n2.   Bowling -----> 100 Rs./HOURS \n3. Sight of the Serpent –	----> 250 Rs./HOURS \n4. Karting ----> 400 Rs./HOURS \n5. 	Video Games -----> 300 Rs./HOURS \n6.Swimming Pool Games-----> 350 Rs./HOURS \n7. Exit\n""")

   game=int(input("Enter The Game You Want To Play : "))
   hour=int(input("Enter No. Of Hours You Want To Play : "))
   print("\n\n*************************************************\n")

   if game==1:
      print("YOU HAVE SELECTED TO PLAY : Table Tennis")
      gamingbill = hour * 150

   elif game==2:
      print("YOU HAVE SELECTED TO PLAY : Bowling")
      gamingbill = hour * 100

   elif game==3:
      print("YOU HAVE SELECTED TO PLAY : Sight of the Serpent")
      gamingbill = hour * 250

   elif game==4:
      print("YOU HAVE SELECTED TO PLAY : Karting ")
      gamingbill = hour * 400

   elif game==5:
      print("YOU HAVE SELECTED TO PLAY : Video Games")
      gamingbill = hour * 300

   elif game ==6:
      print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")

   elif game ==7:
      return

   else:
      print('Invalid Input')
      return
      print("Your Total Gaming Bill=Rs",gamingbill,"\n")


   with open(Hotel_database, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      data =[]
      for i in reader:
         if len(i) > 1:
            if i[0] == str(ID):
               i[13] = eval(i[13]) + gamingbill
               i[14] = eval(i[14]) + gamingbill
               data.append(i)
            else:
               data.append(i)


   with open(Hotel_database, "w", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerows(data)

   print(input('\nPress any key to continue'))
   return

###########################################################

def laundrybill():
   ID = input('Enter Customer ID : ')
   print("\n******LAUNDRY MENU*******\n")

   print("1.Shorts----->Rs3 \n2.Trousers----->Rs4 \n3.Shirt--->Rs5 \n4.Jeans---->Rs6 \n5.Girlsuit--->Rs8 \n6.Exit\n")
   laundry=int(input("Enter your choice:"))
   quantity=int(input("Enter the quantity:"))

   if (laundry==1):
      lbill = laundry * quantity
   elif (laundry==2):
      lbill = laundry * quantity
   elif (laundry==3):
      lbill = laundry * quantity
   elif (laundry==4):
      lbill = laundry * quantity
   elif (laundry==5):
      lbill = laundry * quantity
   elif (laundry==6):
      return
   else:
      print("Invalid option")
      return
   print("Your Total Laundry Bill=Rs",lbill,"\n")

   with open(Hotel_database, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      data =[]
      for i in reader:
         if len(i) > 1:
            if i[0] == str(ID):
               i[12] = eval(i[12]) + lbill
               i[14] = eval(i[14]) + lbill
               data.append(i)
            else:
               data.append(i)


   with open(Hotel_database, "w", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerows(data)

   print(input('\nPress any key to continue'))
   return

###########################################################

def search():
   Name = input('Enter Customer Name You Want To Search: ')
   with open(Hotel_database, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      count = 0
      data =[]
      for i in reader:
         if len(i) > 1:
            if i[1].lower() == Name.lower():
               print(i[0:7])
               count = count + 1
      if count == 0:
         print('No Customer Data Found!')

      print(input('\nPress any key to continue'))
###########################################################
def totalbill():
   global Hotel_database
   global Hotel_fields
   ID = input('Enter Customer ID : ')
   print ("\n******HOTEL BILL******")
   with open('Hotelrecord.csv', "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      data =[]
      for i in reader:
         if len(i) > 1:
               if i[0] == str(ID):
                  for j in range(0,15):
                     print('\nCustomer',Hotel_fields[j],' :',i[j])
   print(input('\nPress any key to continue'))
   return

while(True):
   print("""
   1--->Enter Customer Details
   2--->Calculate Restaurant Bill
   3--->Calculate Laundry Bill
   4--->Calculate Game Bill
   5--->Search Customer
   6--->GENERATE TOTAL BILL AMOUNT
   7--->EXIT """)

   choice = int(input("Enter Your Choice : "))
   if choice == 1:
      add_Customer()
   elif choice ==2:
      restaurentbill()
   elif choice == 3:
      laundrybill()
   elif choice ==4:
      gamingbill()
   elif choice ==5:
      search()
   elif choice ==6:
      totalbill()
   elif choice ==7:
      print("-------------------------------")
      print("🙏 Thank you for using our system 🙏")
      print("-------------------------------")
      break

sys.exit()
