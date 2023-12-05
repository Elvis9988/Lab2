# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

#taking user input
start = int(input("Enter the number of calories daily intake: "))

#using if else
if (start < 0):
    print ("Do it again")
else:
    print()
        
#assigning values
decrease = float(input("Enter the decrease in calories: "))
days = int(input("Enter the number of days you would like to calculate "))

#using for loop
for i in range(days):
        start = start - ((decrease * start)/100)
        if start < 1200:
            print ("You need to stabilize your diet")
            break
        else:
            print ("Decrease in calories per day :", start)

    
        
        
    
        