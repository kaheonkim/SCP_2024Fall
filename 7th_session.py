A = [1,2,7,8]

# First entry
# print(A[0])

# Last entry
# print(A[3])
# print(A[-1])

# second Last entry
# print(A[-2])

#[7,8]
# print(A[1:3])

# length
# print(len(A))

#max, min
# print(max(A))
# print(min(A))

#sum
# print(sum(A))

# Appending

# A.append(10)
# print(A)


#remove
# A.remove(2)
# print(A)

#pop
# A.pop(2)
# print(A)

B = [1,3,2,1.4]

#sort
# print(sorted(B))

# B.reverse()
# print(B)

#concatenation
# print(A+B)

# repeating
# print(A*3)


# mean
# def mean(l):
#     return sum(l)/len(l)




# check by printing
# for i in range(len(A)):
#     print(A[i])
    
# for a in A:
#     print(a)

#add squared sum
# def squared_sum(l):
#     s = 0
#     for i in range(len(l)):
#         s += l[i]**2
#     return s

# def squared_sum(l):
#     s = 0
#     for a in l:
#         s += a**2
#     return s

def squared_sum(l):
    l_ = [a ** 2 for a in l]
    return sum(l_)

def find_max_ind(l):
    maximum = max(l)
    output = []
    for i in range(len(l)):
        if l[i] == maximum:
            output.append(i)
    return output

def even_num(l):
    output1, output2 = [], []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            output1.append(l[i])
            output2.append(i)
    return output1, output2