# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

def get_bonus(salary, us):
    if(us>1000):
        bonus=salary*0.2
    elif(us>501 and us<1000):
        bonus=salary*0.1
    return bonus

def nett_salary(salary, bonus):
    nett = salary+bonus
    return nett

def display(i, stsalary, units, bn, ne):
    print("\n~~~~~~~~")
    print("SALARY SLIP")
    print("~~~~~~~~")
    print("Staff ID               :  {}".format(i))
    print("Staff Salary           :  RM {:.2f}".format(stsalary))
    print("Staff Sold             :  {}".format(units))
    print("Bonus                  :  RM {:.2f}".format(bn))
    print("Nett Salary            :  RM {:.2f}".format(ne))


print("~~~~~~~~")
print("DATA ENTRY")
print("~~~~~~~~")
s= input("Enter staff id          : ")
salary = float(input("Enter staff salary      : RM "))
sold= int(input("Enter total units sold  : "))
bonus = get_bonus(salary, sold)
nett  = nett_salary(salary, bonus)
display(s, salary, sold, bonus, nett)

