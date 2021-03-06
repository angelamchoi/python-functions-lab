# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

sum_to(6)  # returns 21
sum_to(10) # returns 55

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num 
  return largest

  def largest(nums):
    nums.sort()
    return nums[-1]

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

#3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(word, subword):
  return word.count(subword)

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0

#4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0
  
### Notes
#  Python Parameter specific (*args)
# def f(*args): #// always after
#   #what data type
#   print( type(args) ) #gives us tuples
#   for arg in args:
#     print(arg)