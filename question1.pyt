# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

#taking input from users
years = int(input("Enter the number of years: "))
years = years * 12
i = 1
temp = 0

#using while loop
while i <= years:
    i=1
    z = 0
    while i <= 12:
        months = int(input("Enter average high temperature for month" + str(i) + ": "))
        if months>z:
            z = months
        temp = temp + months
        i = i+1
    
    print ("Highest temperature for the year :", z)
    print ("Average high temperature for the year :" , (temp/12))
    

    
    
    

    