s = 0
for i in range(12):
    s+= 100*1.02**i
print(s)

s = 0
i = 0
while s < 10000:
    i += 1
    s+= 100 * 1.02**(i-1)
print(i)