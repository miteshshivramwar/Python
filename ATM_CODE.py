# Create ATM Data for backend
import csv
atm_info = {}
atm_info[card_pin] = {3333:{"Name":"John C" ,"Card_Status":"Active", "CardNum":1234, "Saving_Account_Balance" : 100, "Current_Account_Balance":0, "Mobile":9898989898, "OTP": "67675"},
2838:{"Name":"Gary Mac" ,"Card_Status":"Active" ,"CardNum":4322 ,"Saving_Account_Balance": 1200 ,"Current_Account_Balance": 4000,"Mobile":999955555,"OTP": "86845"}
                    }
otp = None
amt_withdraw = None
opt_3 = None
opt = None
new_pin =None
mobile = None
latest_bal = None

#Disply Options to the user on ATM Screen
print("Welcome to XYZ bank")
input_pin = int(input("Please enter pin"))
rec = atm_info[card_pin]
print("Please select options from the below menu")
print("Press 1 for Mini Statement")
print("Press 2 for Withdrwal")
print("Press 3 for Others")
print("Press 4 to exit") 
opt = int(input("Please select options from the menu"))

if opt == 2:
    amt_withdraw = float(input("Enter the amount to be withdrwan"))
elif opt == 3:
    print("Press A for PIN Exchange")
    print("Press B for Blocking Card")
    opt_3 = input("Please input your choice")
    if opt_3 == "A":
        new_pin = input("Input new Pin")
        mobile = int(input("Enter 10 digit mobile number") )
        otp =  int(input("Enter OTP") )
    elif opt_3 == "B" :
        mobile = int(input("Enter 10 digit mobile number") )
        otp =  int(input("Enter OTP"))
for key,value in rec.items():
    if key == input_pin:
        print("Card accepted")
        for k1,v1 in value.items():
            
            print("My Option is ",opt,k1)
            if opt == 2 and k1 == "Saving_Account_Balance" :
                print("Inside Withdrawl")
                if amt_withdraw> v1:
                    print("Low Balance")
                    break
                else:
                    latest_bal = v1-amt_withdraw
                    atm_info[card_pin][k1] = lates_bal
                    print("Transaction Successful ; Available Balance Post Withdrawl >> ",latest_bal)
                    break
            
            elif opt_3=="A" and key==input_pin:
                print("Inside Pin Change")
                atm_info[card_pin][key] = new_pin
                print("Transaction Successful ; Pin Change Successful ")
                break
            
            
            elif opt_3=="B" and k1=="Card_Status" :
                
                
                print("Inside Block Card")
                atm_info[card_pin][k1] = "Blocked"
                print("Transaction Successful ; Card blocked ")
                break 
            else:
                print("hiii",v1)
                atm_info[card_pin][k1]=v1
                

            
        
    break

print("Thank You")
a_file = open("C:\GIT\sample1.csv", "w")
writer = csv.writer(a_file)
for key, value in rec.items():
    writer.writerow([key, value])

a_file.close()
