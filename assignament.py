# (Q1) 
# Q1.Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest 
# and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution

def minmax(data):
    if data != []:
        min = data[0]
        max = data[0]
        for item in data:
            if min>item:
                min = item
            if max<item:
                max = item
        
        return tuple((min,max))

 

print(minmax([1,2,3,4,5,6]))
print(minmax([4,2,5,4,5,6]))
print(minmax([]))
print(minmax([2,35,6]))

# ----------------------------------------------------------------------------------------------------------------------------------

# Q2.   What would be the output of the following code snippet and why?
def scale(data, factor):
  for val in data:
    val *= factor

data = [1,2,3,4,5]; 
print (data)

scale(data, 5)
print (data)

# ans : date will not be changed as as copy of list is being modified

# ----------------------------------------------------------------------------------------------------------------------------------
#Q3 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.

def sqr(n):
   sum = 0
   for i in  range(1,n):
      sum+=i*i
    
   return sum

print(sqr(5))

# ----------------------------------------------------------------------------------------------------------------------------------

#Q4  Give a single command that computes the sum from Q2, relying on Python’s comprehension syntax and the built-in sum function.
l1 = [1,2,3,4,5]
total = 0
[total := total + x for x in [1, 2, 3, 4, 5]]
print(total)
 # ----------------------------------------------------------------------------------------------------------------------------------
#  Q5 and Q6 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
def pattern():
   for item in range(8,-9,-2):
      print(item,end=" ")

pattern()

# ----------------------------------------------------------------------------------------------------------------------------------
# Q7.In the below code, the body of the loop executes the command data[j] = factor. We have discussed that numeric types are immutable, and that use of the = operator in this context causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?


def scale(data, factor,var):
    for j in range(len(data)):
        data[j] = factor

    var = 45
       
list1 = [1,2,3,4]
var = 4
print(list1,var)
scale(data,4,var)
print(list1,var)
# ans here the variable is also passed and everytime we change that varibale than new instance is created and original is not changed . but when we are passing list 
# than list object is created and stored in the original list

# ----------------------------------------------------------------------------------------------------------------------------------
# # Q8. Given the code snippet below answer the following questions:
my_list = [[1, 2, 3], 4, 5]
another_list = my_list.copy()
another_list[0] += [6,]
my_list.append(8)
print(my_list)
print(another_list)

# 1.    What would be the output and the reason behind it?
# ans 
# the inner list will be changed as we are using  += operator . it will change the orignal inner list and for outer list we will not have any change as copy is passed 


# 2.    Will the second operation reflect in both lists? If so how to ensure that any change in my_list[0] doesnt reflect in another_list
# ans 
# another_list[0] = another_list[0]+ [6,]
# by using the above command we can stop the change of inner list 

# ----------------------------------------------------------------------------------------------------------------------------------
# Q9.      Given the code snippet below, what would be the output and why?

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)

print(xs) 
print(ys) # we have given  a new list to the ys 

xs.append(['new sublist'])
print(xs)
print(ys) # only changes will be shown i  x as appened in x and y is a new list

xs[1][0] = 'X'
print(xs)
print(ys) # both list will be changed as element of xs is changed 
# ----------------------------------------------------------------------------------------------------------------------------------

# Q10. Write a Python class, Flower, that has three instance variables of type str, int, and float, 
# that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor
#  method that initializes each variable to an appropriate value, 
# and your class should include methods for setting the value of each type, and retrieving the value of each type.
class Flower():
    def __init__(self, flower, petals, price):
      self.flower = flower
      self.petals = petals
      self.price = price

    def desc(self):
      return(f"{self.flower} has {self.petals} petals and it costs {self.price} rupees")

    def set_flower_name(self,flower):
       self.flower = flower

    def set_petals(self,petals):
       self.petals = petals

    def set_price(self,price):
       self.price = price

tulip = Flower("tulip",4,23.3)
rose = Flower("rose",10,120.3)

print(tulip.desc())
print(rose.desc())

tulip.set_price(110)
print(tulip.desc())


