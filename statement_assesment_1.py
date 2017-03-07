# #1
# st = 'Print only the words that start with s in this sentence'
#
# string = st.split()
# for word in string:
#     if word.startswith('s'):
#         print word
# 2 Use range() to print all the even numbers from 0 to 10.

# print range(0,10,2)
# 3 Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# ls = [ x for x in range(1, 50) if x % 3 == 0]
# print ls
# #4 Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
# word = st.split()
# for i in word:
#     x = len(i)
#     if x %2 == 0:
#         print "even is", x
# 5
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# for i in range(1,101):
#     if i % 3 == 0:
#         print "Fizz"
#     elif i % 5 == 0:
#         print "Buzz"
#     elif i % 3 == 0 and i % 5 == 0:
#         print "FizzBuzz"
#     else:
#         print i
# 6
# Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'
# ls = [ word[0] for word in st.split()]
