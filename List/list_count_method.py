# The count() method returns the number of times the specified element appears in the list.

# Syntax of List count()
# list.count(element)

""" Example 1: Use of count() """
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

""" Example 2: Count Tuple and List Elements Inside List """

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)