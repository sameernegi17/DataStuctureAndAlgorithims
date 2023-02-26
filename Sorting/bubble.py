def bubble_sort(arr):
    for i in range(0,len(arr)):
        print(f"------- {i} : {arr}")
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"j {j}  : {arr}")
    return arr

print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))