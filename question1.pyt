#taking input from users
years = int(input("Enter the number of years: "))
years = years * 12
i = 1
temp = 0
while i <= years:
    i=1
    while i <= 12:
        months = int(input("Enter average high temperature for month" + str(i) + ": "))
        temp = temp + months
        i = i+1
    
    print ("Average high temperature for the year :" , (temp/12))
    

    
    
    

    