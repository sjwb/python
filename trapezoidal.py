import math
def fn(x):
    return x   #Integration of function f(x)=x
a,b,s=int(input('lower limit:')),int(input('upper limit:')),0
h=(b-a)/24  #I use 24 interval
for i in range(1,24):
    s=s+fn(a+i*h)
m=(h/2)*(2*s+fn(a)+fn(b))
print(f'Value of integration is {m}')
