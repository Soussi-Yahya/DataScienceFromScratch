
"""
grades = {"Joel" : 80 , "Tim" : 95}

joels_grades  = grades["Joel"]


print (joels_grades)

try :
    kates_grades = grades["Kate"]
except KeyError :
    print("no grades for kate!!")
    
    
    
print("Kates" in grades)
"""


"""
tweet = {
 "user" : "joelgrus",
 "text" : "Data Science is Awesome",
 "retweet_count" : 100,
 "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()


print("user" in tweet_keys )
print("user" in tweet)
print("joelgrus" in tweet_values )




document = "Hello this is a test document to test the approach of the functions created below"


word_counts = {}

for word in document :
    if word in word_counts :
        word_counts[word] += 1
    else :
        word_counts[word] = 1
print (word_counts)

"""
"""

def some_function_that_return_a_string() :
    return input()

"""
#s = some_function_that_return_a_string()
"""
if s :
    first_char = s[0]
else :
    first_char = ""
    
    
"""

"""
IMPORTANT NOTE !!! :
the and operand in python does not return true or false , it returns one of its operand !!
exp :
A and B
1 . if A is falsy , return A
2 . if A is truthy , return B

note : falsy values include ; ""  , 0 , None , False , [] , {}
"""
"""
first_char_2 = s and s[0]


print(f"first char using the second method : {first_char_2}")
"""

#the not so basic section
"""
this is just sorting , pretty basic , you just apply sorting to the list by invoking the sort() method
x = [4,1,2,6]
y = sorted(x)
print(x,y)
x.sort()
print(x)
"""
###############################################
#list comprehensions
###############################################

"""
#we need to get limited number(3 in this case) of even numbers pythonic wayyy  ^-^
even_numbers = [x for x in range(5) if x % 2 == 0]
#print(even_numbers)

squares = [x * x for x in range(5)]
#print(squares)

#this is pretty match self explanatory , we'll get the square of each number in the even list 
even_squares = [x*x for x in even_numbers]
#print(even_squares)

#we created a dict , key: value pair , where the key is the number and the valeue is its square 
square_dict = {x:x*x for x in range(5)}
#print(square_dict)


square_set = {x*x for x in [1,-1]}
#print(square_set)

#if you dont need the value from the list its conventional to use an underscore as the variable 

#zeroes = [0 for _ in even_numbers]


#!!! a list comprehension can include multiple fors :

pairs = [(x,y) for x in range(2) for y in range(2)]
print(pairs)


#For each number x from 0 to 4,
#it chooses y as every number greater than x up to 4.


inc_pairs = [(x,y) for x in range(5)
             for y in range(x+1,5)]
             
print(inc_pairs)

"""


#generators and iterators ^_^

"""
generators by definition : something that you can iterate over
but whose values are produced only as needed (lazily)

!!!!!!!in other words : a generator does not create all the items at once 


NOTE!!!!! : please note that in python 3 and above , range itself is lazy

Uses almost no memory
Good for large or infinite sequences
Good for streaming data
"""


"""
def lazy_range(n) :
    i = 0
    while i < n  :
        yield i
        """
"""
        !!!!!!!!
        yield means  , pause the function ,
        send one value to the caller ,
        resume when the next value is requested
        """
        #i+=1
"""
#will consume the yielded values one at a time until none are left        
for i in lazy_range(10) :
    print(i)


### !!!! infinite generator

def natural_numbers():
    n = 1
    while True  :
        yield n
        n+=1
####this is an infine sequence
#but if you try
        """
"""
for x in natural_numbers() :
 
    print(x)
    
    """
#this loop will never stop
#so you'd need something like
"""
for x in natural_numbers():
    if x > 10 :
        break
    print(x)

"""
    
    
    
    
#Randomness
    
import random
four_uniform_random = [random.random() for _ in range(4)]
#random.random generates numbesr betwenn 0 and 1 

#print(four_uniform_random)

#with seed
print(f"{'-'*10} with seed {'-'*10} ")
#you can play around here to test the seed behavior
random.seed(10)
for t in range(2) :
    random.seed(778)
    print("x"*5)
    for i in range (5) :
        random.seed(random.random())
            
        print (random.random())
"""
print(random.random())
random.seed(10)
print(random.random())
"""

#without seed 

print(f"{'-'*10} without seed {'-'*10} ")
print(random.random())
print(random.random())


#seed explanation and why do we need it \OwO/

"""
a seed is just a number you give to hte random number generator so that it
starts in a known state

ig ; 
print(f"{'-'*10} with seed {'-'*10} ")
will give you always the same ****first number*** 
without a seed python uses you system clock and the numbers will be
different every run


but why does seeding make numbers repeat  :
because computers cannot do true randomness
they produce fake randomness (pseudorandomess) using math fomulas
if you give the same starting point (the seed) you get the same sequence.


we use seeds when we want reproduccibility
meaning you want your program to behave exactly the same when you run it again or when someone else runs it 

debugginng  , if your code uses randomness , a bug might appear only sometimes ,
but with a seed you'll see the exact same random results every run , easy to debug .

machine learning :
ML modules use randomness(weight initialization , data shuffling)
if you use a seed , you get the same traning results every time , which is important for :
comparing experiments , writing papers , reproducing results 


"""


