a = [5,6,7,8,9,10]


def two_sum(a):
    diff = set()
    for i in range(0,len(a)):
        if a[i] not in diff:
            diff.add(10-a[i])
        else:
            return True
        
    
    return False


print(two_sum(a))
    
               