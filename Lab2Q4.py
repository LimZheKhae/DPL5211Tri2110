#Student ID:1201200825
#Stundent Name:Lim Zhe Khae
banana=1.5
grapes=5.6
qty=int(input("Enter how many comb banana you want to buy : "))
kilo=int(input("Enter how many  of grapes you want to buy :"))
total1=qty*1.5
total2=kilo*5.6
sum=total1+total2
print("Invoice for Fruits Purchase")
print("---------------------------------")
print("\nEnter the quantity (comb) of bananas bought: ",qty)
print("Enter the amount (kg) of grapes bought: ",kilo)
print("Item               \t    Qty    \t     Price    \t   Total")
print("Banana (combs)     \t   ",qty , " \t\tRM ",banana, "\tRM ",total1)
print("Grapes (kg) (combs)\t   ",kilo ," \t\tRM ",grapes, "\tRM ",total2)
print("\n Total: RM ",sum)