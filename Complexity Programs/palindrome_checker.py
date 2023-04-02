"""
A palindrome is a word or phrase that reads the same both forward and
backward. Some examples include “racecar,” “kayak,” and “deified.”

"""

def palindrom_checker(text):
    left_i = 0
    right_i = len(text) -1

    while(left_i < (len(text)/2)):
          if text[left_i] != text[right_i]:
            return False
          
          left_i +=1
          right_i -=1


    return True

print(palindrom_checker("racecar"))
print(palindrom_checker("kayak"))
print(palindrom_checker("sameer"))
