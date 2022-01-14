setOne = []
setTwo = []
setThree = []
setFour = []
setFive = []

#divisible by 7 and 3
for x in range(1, 101):
    if (x%7==0) and (x%3==0):
      setOne.append(str(x))
print ("This is a set of numbers between 1 and 100 that are divisible by 7 and 3: ")
print (','.join(setOne))



#divisible by 7, but not 3
for x in range(1, 101):
    if (x%7==0) and (x%3!=0):
      setTwo.append(str(x))
print ("This is a set of numbers between 1 and 100 that are divisible by 7, but not 3: ")
print (','.join(setTwo))


#divisible by 7 but not 3
for x in range(1, 101):
    if (x%2!=0 and x%7==0) and (x%3!=0):
      setThree.append(str(x))
print ("This is a set of ODD numbers divisible by 7 but not 3: ")
print (','.join(setThree))


#Harshad numbers
for x in range(1,101):
  # Initialising sum and remainder to 0
  sum = rem = 0 
  #Make a copy of x and store it in variable num 
  num=x
  #Calculates sum of digits  
  while(num > 0):  
    rem = num%10;  
    sum = sum + rem;  
    num = num//10;   #this returns the floor value
  if(x%sum == 0):  
    setFour.append(str(x))
print ("This is a set of numbers that are divisible by the sum of its digits (Harshad numbers) : ")
print (','.join(setFour))



#numbers that are equal to the square of the sum of its digits
for x in range(1,101):
  # Initialising sum and remainder to 0
  sum = rem = 0 
  #Make a copy of x and store it in variable num 
  num=x
  #Calculates sum of digits  
  while(num > 0):  
    rem = num%10;  
    sum = sum + rem;  
    num = num//10;   #this returns the floor value
  if(x == (sum**2)):  
    setFive.append(str(x))
print ("This is a set of numbers that are equal to the square of the sum of its digits : ")
print (','.join(setFive))
