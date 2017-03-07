1# 1 Write a function that computes the volume of a sphere given its radius.
import math


def vol(rad):
    return 4.0/3 * math.pi * rad**3

# 2 Write a function that checks whether a number is in a given range (Inclusive of high and low)


def ran_check(num, low, high):
    if num >= low and num <= high:
        return "Num is in range"
    else:
        return "Num out of range"

def ran_check(num, low, high):
# Check if num is between low and high (including low and high)
    if num in range(low, high + 1):
        print " %s is in the range" % str(num)
    else:
        print "The number is outside the range."
# 3 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# def up_low(s):
#     count_upper = 0
#     count_lower = 0
#     for i in s:
#         if i.isupper():
#             count_upper += 1
#         if i.islower():
#             count_lower += 1
#     print 'No. of Upper case characters : ', str(count_upper)
#     print 'No. of Lower case Characters : ', str(count_lower)
# 4 Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def unique_list(l):
#     return list(set(l))
# print unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
# 5 Write a Python function to multiply all the numbers in a list.

# def multiply(numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total
# 6 Write a Python function that checks whether a passed string is palindrome or not.
# def palindrome(s):
#     if s == s[::-1]:
#         return "True"
#     else:
#        return "False"
# def palindrome(s):
#     s = s.replace(' ',
#                   '')  # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
#     return s == s[::-1]  # Check through slicing
# 7 Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)  
#     return alphaset <= set(str1.lower())