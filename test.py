my= (1,2,3,4,5)
result = my[1:4:2]
print(result)
#the result will be (2,4)
#this is because the first number is the starting point, the second number is the ending point, and the third number is the step
#thus the starting point is 1, the ending point is 4, and the step is 2
#the reason why it not 5 is because the ending point is not inclusive
#the reason 4 is included is because the step is 2, so it will include the number 4
#the reaosn 4 is the endpoint is because the step is 2, so it will not include the number 5



smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)