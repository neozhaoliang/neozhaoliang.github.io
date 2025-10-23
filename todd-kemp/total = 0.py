i = 1
li = []
n = 10000000000000000000
while i < n:
    li.append(1.0 / i)
    i += 1

print(sum(li))
