def func(a,A):
    if a in A:
        print('yes')
    else:
        print('no')
        
A = {1,1,2,3}
# A.add(4)
# A.remove(2)
# A.add(-3)
print(list(A))

LIST = [1,2,1,5]
print(set(LIST))

B = {2,3,4}
# print(A)
# print(len(A))
# print(max(A))
# print(min(A))

# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))

A = [1,-1,2,-2,3,-3,4]

def squares(A):
    empty = []
    for a in A:
        if a not in empty:
            empty.append(a**2)
    return sorted(empty)



def squares(A):
    empty = []
    for a in A:
        empty.append(a**2)
    return sorted(list(set(empty)))

my_set = {3, 1, 4, 2}
print(my_set)


A = {1:3, 4:'a','b':10}
print(A[1])
print(A[4])
print(A['b'])

A[3] = 'new'
print(A)

A[1] = '3'
print(A)

print(A.keys())
print(A.values())

def factor_to_value(pairs):
    prod = 1
    basis = pairs.keys()
    for base in basis:
        prod *= base**(pairs[base])
    return prod
        