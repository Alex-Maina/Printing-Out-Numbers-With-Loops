setOne = []
setTwo = []
setThree = []
setFour = []
setFive = []

for x in range(1, 101):

    #divisible by 7 and 3
    if (x%7==0) and (x%3==0):
      setOne.append(str(x))


    #divisible by 7, but not 3
    if (x%7==0) and (x%3!=0):
      setTwo.append(str(x))


    #Odd numbers divisible by 7 but not 3
    if (x%2!=0 and x%7==0) and (x%3!=0):
      setThree.append(str(x))
    

    #Harshad numbers
    def harshad (num):
        # Initialising sum and remainder to 0
        sum = rem = 0 

        #Make a copy of num and store it in variable n 
        n = num

        #Calculates sum of digits  
        while(num > 0):  
            rem = num%10 
            sum = sum + rem  
            num = num//10   #this returns the floor value
        if(n%sum == 0):  
            setFour.append(str(n))

    harshad (x)


    #equal to the square of the sum of its digits
    def square_sum (num):
        # Initialising sum and remainder to 0
        sum = rem = 0 

        #Make a copy of num and store it in variable n 
        n = num

        #Calculates sum of digits  
        while(num > 0):  
            rem = num%10 
            sum = sum + rem  
            num = num//10   #this returns the floor value
        if(x == (sum**2)):  
            setFive.append(str(x))

    square_sum (x)    
    

#Let's print each list as a sring where those values are separated by a comma
print ("This is a set of numbers between 1 and 100 that are divisible by 7 and 3: ")
print (','.join(setOne))

    
print ("This is a set of numbers between 1 and 100 that are divisible by 7, but not 3: ")
print (','.join(setTwo))


print ("This is a set of ODD numbers divisible by 7 but not 3: ")
print (','.join(setThree))


print ("This is a set of numbers that are divisible by the sum of its digits (Harshad numbers) : ")
print (','.join(setFour))


print ("This is a set of numbers that are equal to the square of the sum of its digits : ")
print (','.join(setFive))
