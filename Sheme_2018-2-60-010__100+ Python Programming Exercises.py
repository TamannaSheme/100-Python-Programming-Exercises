"""Question 1
Level 1
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
#Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))
#----------------------------------------#

"""Question 2
Level 1
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

#Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input("Enter your value: "))
print (fact(x))
#----------------------------------------#
"""
Question 3
Level 1
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
#Solution:
n=int(input("Enter your value: "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)
#----------------------------------------#
"""Question 4
Level 1
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

#Solution:
values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)
#----------------------------------------#
"""Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

#Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
#----------------------------------------#
"""Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

#Solution:
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))
#----------------------------------------#
"""Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

#Solution:
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)
#----------------------------------------#
"""Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

#Solution:
items=[x for x in input().split(',')]
items.sort()
print (','.join(items))
#----------------------------------------#
"""Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""
#Solution:
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)
#----------------------------------------#

"""Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

"""
#Solution:

s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))

#----------------------------------------#

#----------------------------------------#
"""Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""
#Solution:

from numpy import intp
value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))
#----------------------------------------#

#----------------------------------------#
"""Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
#Solution:

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))
#----------------------------------------#
#----------------------------------------#
"""Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
#Solution:

s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])
#----------------------------------------#
#----------------------------------------#
"""Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
#Solution:

a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)
#----------------------------------------#

#----------------------------------------#
"""Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
#Solution:

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))
#----------------------------------------#
#----------------------------------------#
"""Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""
#Solution:

netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)
#----------------------------------------#

#----------------------------------------#
"""Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

"""
#Solution:

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))
#----------------------------------------#
#----------------------------------------#
"""Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""
#Solution:

from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))
#----------------------------------------#
#----------------------------------------#
"""Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

"""
#Solution:

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reversed(100):
    print (i)
#----------------------------------------#

#----------------------------------------#
"""Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
#Solution:

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
#----------------------------------------#
#----------------------------------------#
"""Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
#Solution:
freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print ("%s:%d" % (w,freq[w]))
#----------------------------------------#

#----------------------------------------#
"""Question 23
level 1

Question:
    Write a method which can calculate square value of number
"""
#Solution:
def square(num):
    return num ** 2

print (square(2))
print (square(3))
#----------------------------------------#

#----------------------------------------#
"""Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
"""
#Solution:
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)

def square(num):
    '''Return the square value of the input number.

    The input number must be integer.
    '''
    return num ** 2

print (square(2))
print (square.__doc__)
#----------------------------------------#
#----------------------------------------#
"""Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.
"""
#Solution:
class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))

#----------------------------------------#

#----------------------------------------#
"""Question 26:
Define a function which can compute the sum of two numbers.
"""
#Solution:
def printValue(n):
	print (str(n))
printValue(3)
#----------------------------------------#
#----------------------------------------#
"""Question 27:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
"""
#Solution:
def printValue(s1,s2):
	print (int(s1)+int(s2))

printValue("3","4")
#----------------------------------------#

#----------------------------------------#
"""Question 28:
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""
#Solution:
def printValue(s1,s2):
	print (s1+s2)

printValue("3","4")
#----------------------------------------#
#----------------------------------------#
"""Question 29 :
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

"""
#Solution:
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print (s1)
	elif len2>len1:
		print( s2 )
	else:
		print (s1)
		print (s2)


printValue("one","three")
#----------------------------------------#

#----------------------------------------#
"""Question 30:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

"""
#Solution:
def checkValue(n):
	if n%2 == 0:
		print ("It is an even number")
	else:
		print ("It is an odd number")

checkValue(7)
#----------------------------------------#
#----------------------------------------#
"""Question 31:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
"""
#Solution:
def printDict():
	d=dict()
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print (d)
#----------------------------------------#
#----------------------------------------#
"""Question 32:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
"""
#Solution:
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print (d)

printDict()
#----------------------------------------#
#----------------------------------------#
"""Question 33:

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

"""
#Solution:
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():
		print (v)

printDict()
#----------------------------------------#
#----------------------------------------#
"""Question 34:

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

"""
#Solution:
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():
		print (k)


printDict()
#----------------------------------------#
#----------------------------------------#
"""Question 35:

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

"""
#Solution:
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li)


printList()

#----------------------------------------#
#----------------------------------------#
"""Question 36:

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

"""
#Solution:
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[:5])


printList()


#----------------------------------------#

"""Question 37:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
"""
#Solution:
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[-5:])
printList()

#----------------------------------------#
"""Question 38:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
"""
#Solution:
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[5:])


printList()

#----------------------------------------#
"""Question 39:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
"""
#Solution:
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (tuple(li))

printTuple()


#----------------------------------------#
"""Question 40:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
"""
#Solution:
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print (tp1)
print (tp2)

#----------------------------------------#

"""Question 41:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""
#Solution:
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2 == 0:
		li.append(tp[i])

tp2 = tuple(li)
print (tp2)

#----------------------------------------#

"""Question 42:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""
#Solution:
s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print ("Yes")
else:
    print ("No")
#----------------------------------------#

"""Question 43:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
"""
#Solution:
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print (evenNumbers)

#----------------------------------------#
"""Question 44:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""
#Solution:
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print (squaredNumbers)

#----------------------------------------#
"""Question 45:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
#Solution:
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (evenNumbers)

#----------------------------------------#
"""Question 46:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""
#Solution:
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print (evenNumbers)

#----------------------------------------#
"""Question 47:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""
#Solution:
squaredNumbers = map(lambda x: x**2, range(1,21))
print (squaredNumbers)

#----------------------------------------#
"""Question 48:
Define a class named American which has a static method called printNationality.
"""
#Solution:
class American(object):
    @staticmethod
    def printNationality():
        print ("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

#----------------------------------------#
"""Question 49:
Define a class named American and its subclass NewYorker. 
"""
#Solution:

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print (anAmerican)
print (aNewYorker)

#----------------------------------------#
"""Question 50:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
"""
#Solution:

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print (aCircle.area())

#----------------------------------------#

"""Question 51:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
"""
#Solution:
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print (aRectangle.area())
#----------------------------------------#

"""Question 52:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
#Solution:
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print (aSquare.area())
#----------------------------------------#
"""Question 53:
Please raise a RuntimeError exception."""
#Solution:
raise RuntimeError('something wrong')

#----------------------------------------#
"""
Question 54:
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
#Solution:
def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception as err:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')

#----------------------------------------#
"""Question 55:
Define a custom exception class which takes a string message as attribute.
"""
#Solution:
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
#----------------------------------------#
"""Question 56:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
"""
#Solution:
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))

#----------------------------------------#
"""Question 57:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
"""
#Solution:
import re
emailAddress = raw_input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print (r2.group(2))

#----------------------------------------#
"""Question 58:
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
"""
#Solution:

import re
s = input()
print (re.findall("\d+",s))

#----------------------------------------#
"""Question 59:
Print a unicode string "hello world".
"""
#Solution:
unicodeString = u"hello world!"
print (unicodeString)

#----------------------------------------#
"""Question 60:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""
#Solution:
s = input()
u = unicode( s ,"utf-8")
print (u)

#----------------------------------------#

"""Question 61:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)."""
#Solution:
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print (sum)
#----------------------------------------#

"""Question 62:
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0)."""
#Solution:
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print (f(n))
#----------------------------------------#
"""Question 63:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console."""
#Solution:
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print (f(n))

#----------------------------------------#
"""
Question 64:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
"""
#Solution:
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print (",".join(values))

#----------------------------------------#
"""Question 65:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

"""
#Solution:
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))
#----------------------------------------#
"""Question 66:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
"""
#Solution:
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print (",".join(values))

#----------------------------------------#
"""Question 67:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"""
#Solution:
li = [2,4,6,8]
for i in li:
    assert i%2==0
#----------------------------------------#
"""Question 68:
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
"""
#Solution:

expression = input()
print (eval(expression))

#----------------------------------------#
"""Question 69:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

"""
#Solution:
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print (bin_search(li,11))
print (bin_search(li,12))

#----------------------------------------#
"""Question 70:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"""
#Solution:
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print (bin_search(li,11))
print (bin_search(li,12))

#----------------------------------------#

"""Question 71:
Please generate a random float where the value is between 10 and 100 using Python math module.
"""
#Solution:
import random
print (random.random()*100)
#----------------------------------------#

"""Question 72:
Please generate a random float where the value is between 5 and 95 using Python math module.
"""
#Solution:
import random
print (random.random()*100-5)
#----------------------------------------#
"""Question 73:
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
"""
#Solution:
import random
print (random.choice([i for i in range(11) if i%2==0]))

#----------------------------------------#
"""
Question 74:
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
"""
#Solution:
import random
print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))

#----------------------------------------#
"""Question 75:
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
"""
#Solution:
import random
print (random.sample(range(100), 5))
#----------------------------------------#
"""Question 76:
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
"""
#Solution:
import random
print (random.sample([i for i in range(100,201) if i%2==0], 5))

#----------------------------------------#
"""Question 77:
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""
#Solution:
import random
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

#----------------------------------------#
"""Question 78:
Please write a program to randomly print a integer number between 7 and 15 inclusive.
"""
#Solution:
import random
print (random.randrange(7,16))

#----------------------------------------#
"""Question 79:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""
#Solution:
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print (t)
print (zlib.decompress(t))

#----------------------------------------#
"""Question 80:
Please write a program to print the running time of execution of "1+1" for 100 times.
"""
#Solution:
from timeit import Timer
t = Timer("for i in range(100):1+1")
print (t.timeit())

#----------------------------------------#
"""Question 81:
Please write a program to shuffle and print the list [3,6,7,8]."""
# Solution:
from random import shuffle

li = [3, 6, 7, 8]
shuffle(li)
print(li)
# ----------------------------------------#

"""Question 82:
Please write a program to shuffle and print the list [3,6,7,8]."""
# Solution:
from random import shuffle

li = [3, 6, 7, 8]
shuffle(li)
print(li)
# ----------------------------------------#
"""Question 83:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""
# Solution:
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)

# ----------------------------------------#
"""
Question 74:
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""
# Solution:
li = [5, 6, 77, 45, 22, 12, 24]
li = [x for x in li if x % 2 != 0]
print(li)

# ----------------------------------------#
"""Question 85:
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""
# Solution:
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for x in li if x % 5 != 0 and x % 7 != 0]
print(li)
# ----------------------------------------#
"""Question 86:
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""
# Solution:
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i % 2 != 0]
print(li)

# ----------------------------------------#
"""Question 87:
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""
# Solution:
array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)

# ----------------------------------------#
"""Question 88:
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
# Solution:
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(li)

# ----------------------------------------#
"""Question 89:
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
"""
# Solution:
li = [12, 24, 35, 24, 88, 120, 155]
li = [x for x in li if x != 24]
print(li)

# ----------------------------------------#
"""Question 90:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
"""
# Solution:
set1 = set([1, 3, 6, 78, 35, 55])
set2 = set([12, 24, 35, 24, 88, 120, 155])
set1 &= set2
li = list(set1)
print(li)

# ----------------------------------------#
"""Question 91:
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
"""
# Solution:
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print (removeDuplicate(li))
# ----------------------------------------#

"""Question 92:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""
# Solution:
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print (aMale.getGender())
print (aFemale.getGender())
# ----------------------------------------#
"""Question 93:
Please write a program which count and print the numbers of each character in a string input by console.
"""
# Solution:
dic = {}
s=input()
for s in s:
    dic[s] = dic.get(s,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

# ----------------------------------------#
"""
Question 94:
Please write a program which accepts a string from console and print it in reverse order.
"""
# Solution:
s=input()
s = s[::-1]
print (s)
# ----------------------------------------#
"""Question 95:
Please write a program which accepts a string from console and print the characters that have even indexes.
"""
# Solution:
s=input()
s = s[::2]
print (s)
# ----------------------------------------#

"""Question 96:
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
# Solution:
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(li)

# ----------------------------------------#
"""Question 97:
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
"""
# Solution:
li = [12, 24, 35, 24, 88, 120, 155]
li = [x for x in li if x != 24]
print(li)

# ----------------------------------------#
"""Question 98:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
"""
# Solution:
set1 = set([1, 3, 6, 78, 35, 55])
set2 = set([12, 24, 35, 24, 88, 120, 155])
set1 &= set2
li = list(set1)
print(li)

# ----------------------------------------#
"""Question 99:
Please write a program which prints all permutations of [1,2,3]
"""
# Solution:
import itertools
print (list(itertools.permutations([1,2,3])))

# ----------------------------------------#
"""Question 100:
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
"""
# Solution:
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)

# ----------------------------------------#
