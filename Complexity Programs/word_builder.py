

# 2 letter word
def word(arr):
    collections = []

    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if (i != j):
                collections.append(arr[i]+arr[j])

    return collections


print(word(['a','b','c','d']))

#3 letter word

def l3_word(arr):
    collections = []

    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            for k in range(0,len(arr)):
                if (i != j and i != k and j != k):
                    collections.append(arr[i]+arr[j]+arr[k])

    return collections

print(l3_word(['a','b','c','d']))