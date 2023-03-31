

def even_numbers(arr):
    sum = 0
    count = 0

    for item in arr:
        if item % 2 == 0:
            sum += item
            count +=1

    return sum / count

print(even_numbers([1,2,3,4]))
