"""
Quadratic Problem ==> Linear Solution
"""

def hasDuplicates(arr):
    for i in range(0, len(arr)):
        for j in range(1,len(arr)):
             if (i != j and arr[i] == arr[j]):
                return True

    return False


print(hasDuplicates([1,2,3,1]))
print(hasDuplicates([1,2,3]))

print("Linear Solution for Duplicate")
def hasDuplicatesLinear(arr):
    Duplicateset = set()
    for item in arr:
        if item in Duplicateset:
            return True

        Duplicateset.add(item)

    return False  


print(hasDuplicatesLinear([1,2,3,1]))
print(hasDuplicatesLinear([1,2,3]))