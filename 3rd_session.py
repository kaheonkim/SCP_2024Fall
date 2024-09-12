# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu Sep 12 09:12:17 2024

# @author: simonkim
# """

a = 3.5
if a< 5:
    a+= 1
print('a becomes %.1f'%a)



a = int(input('please enter the number(integer)'))
if a % 2 == 0:
    print('It is even')
else:
    print('It is odd')



a = int(input('please enter the number(integer)'))
b = int(input('please enter the number(integer)'))

if a**2 == b or b**2 == a:
    print('they are in square root relation')




a = 3
if a < 0:
    print('a<=0')
elif 0<a<=5:
    print('a is between 0 and 5')
elif 5<a<=10:
    print('a is between 5 and 10')
else:
    print('a is larger than 10')





a = int(input('number'))

sum_ = 0
i = 0
while i <= a:
    sum_ += i
    i += 1
    print(i)
print(sum_)




a, b = 5, 6

sum_ = 0
i = 0
while i <= 15:
    sum_ += 2*3**i
    i += 1
print(sum_)

    



prod = 1
i = 1
while i <= 8:
    prod *= i
    i += 1
print(prod)




s = 0
i = 0
while i <= 100:
    j = 1
    denom = 1
    while (j <=i):
        denom *= j
        j += 1
    s += 5**i/denom
    i+=1
print(s)
   

    

import math
a, b = 5, 6

sum_ = 0
i = 0
while i <= a: 
    j = 0
    while j <= b:
        sum_ += math.log(i**2+j**2+4*i*j+1)
        j += 1
    i+=1
     
print(sum_)




sum_ = 0
x = 0
while x <= 10: 
    y = 0
    while y <= 15:
        if 0 < x < y:
            sum_ += 8*x*y
        y += 1
    x+=1

print(sum_)