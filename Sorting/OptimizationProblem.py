a = [2,8,1]
b = [5,8,3,7,9,10,2,4,1,15,17,19,209,22]

result = []#
count = 0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        count +=1
        if (a[i] == b[j]):
            result.append(a[i])
            break

print(result)
print("Count", count)