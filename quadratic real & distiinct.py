import cmath
print('Enter the value of a ')
a=int(input())
print('Enter the value of b')
b=int(input())
print('Enter the value of c')
c=int(input())
if((b**2)<(4*a*c)):
    print('the roots are imaginary')

if(((b**2)-(4*a*c))==0):
    print('the roots are real and equal')

if(((b**2) - (4*a*c))>0):
    print ('the roots are real and distinct')
    d = (b**2)-(4*a*c)
    print('Enter the value of c')
    c=float(input())
d = (b**2) - (4*a*c)
soll = (-b-cmath.sqrt(d))/(2*a)
sol2 =(-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(soll, sol2))
