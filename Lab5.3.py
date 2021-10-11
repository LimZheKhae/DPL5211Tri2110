#Student ID :1201200825
#Student Name :Lim Zhe Khae
#display the menu
# ask user to enter their choice [1 or 2].
#if choice is 1 call function get_cm()
#if choice is 2 call function get_meter()
# Else print "Invalid choice"
# In get_cm();
#Get the value of centimetre from the user
# Call function cm_to_meter()passs and cm to calculate meter
#Display the centimeter and meter

def cm_to_meter(centimeter):
    meter=centimeter/100
    return meter

def meter_to_cm(meter):
    centimeter=meter*100
    return centimeter

def get_cm():
    cm=float(input("Please enter a value for centimeter: "))
    m=cm_to_meter(cm)
    print("For {} cm is {} m ".format(cm,m))

def get_meter():
    m=float(input("Please enter a value for meter: "))
    cm=meter_to_cm(m)
    print("For {} m is {} cm ".format(m,cm))


choice=int(input("Please Enter your choice, 1 for cm to meter , 2 for meter to cm :"))
if (choice==1):
    get_cm()
elif(choice==2):
    get_meter()

else :
    print("Invalid choice")
