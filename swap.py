a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
print("The numbers before swapping is: " +str(a) +'   '+str(b))
a= a+b
b= a-b
a= a-b
print("The numbers after swapping is: " +str(a) +'  '+str(b))
