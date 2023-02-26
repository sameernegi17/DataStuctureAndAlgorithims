
def selection(arr):
    total_comparison = 0
    total_swapping = 0
    for i in range(0,len(arr)):
        min_index = i
        print(f" array {arr}")
        print(f"Before Search min_index,element : {min_index},{arr[min_index]}")
        comparison = 0
        swapping = 0
        for j in range(i+1,len(arr)):
            comparison +=1
            if arr[j] < arr[min_index]:
                min_index = j

        print(f"After Search min_index,element : {min_index},{arr[min_index]}")
        if i != min_index:
            swapping+=1
            arr[i],arr[min_index] = arr[min_index],arr[i]
        print(f" array {arr}")
        print(f"Compariosn {comparison} , Swapping {swapping}")
        total_comparison += comparison
        total_swapping += swapping
        print("++++++++++++++++++++++++++++")
    

    print(f"Compariosn {total_comparison} , Swapping {total_swapping}")
    return arr



print(selection([5,4,3,2,1]))
