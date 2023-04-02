"""
Array Sample

In this example, we create a function that takes a small sample of an
array. We expect to have very large arrays, so our sample is just the first,
middlemost, and last value from the array

"""

def  sample(array): #N elements
    first = array[0]
    last = array[-1]
    middle_most = array[len(array)//2]

    return [first,last,middle_most]


print(sample([1,2,3,4,5])) #o(1)