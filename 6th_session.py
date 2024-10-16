for i in range(10): 
    print(f"{i:>3}", end=" ")
print()
for i in range(10): 
    print(f"{i:<3}", end=" ")
    
    
n = 123

sum_d = 0

# First Digit

sum_d += n // 100
n %= 100

sum_d += n // 10
n %= 10

sum_d += n % 10


import math
def sum_digit(n):
    remaining_num = n
    sum_digit = 0
    num_digit = int(math.log10(n))
    for i in range(num_digit, 0, -1):
        sum_digit += remaining_num // 10**i
        remaining_num %= 10**i
        print(remaining_num)
        
    sum_digit += remaining_num % 10
    
    return sum_digit