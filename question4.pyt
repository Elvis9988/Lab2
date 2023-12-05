# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# assigning the list
myNumbers = [4,6,9,12,17,22,27,33,44]

print (myNumbers)
 
# using for loop    
for j in range (0,8):
    for i in range (0,8):
        if (myNumbers[i+1])>(myNumbers[i]):
            var = myNumbers[i+1]
            myNumbers[i+1] = myNumbers[i]
            myNumbers[i] = var

print (myNumbers)
    
    