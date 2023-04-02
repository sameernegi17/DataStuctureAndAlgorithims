"""
This function accepts an array of arrays, where the inner arrays
contain 1’s and 0’s. The function then returns how many 1’s there are.
So, for this example input:
[
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1],
[1, 0]
]
"""

def count_the_ones(outer_array):
   count = 0
   for array in outer_array:
      for item in array: 
         if item == 1:
            count +=1

   return count


print(count_the_ones([
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1],
[1, 0]
]))