#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Hello, world!
print("Hello, World!")


# In[2]:


#python If-Else
n= int(input()) 
if (n%2 !=0 or (n%2==0 and 6<n<21)):
    print ("Weird")
else:
    print("Not Weird")


# In[ ]:


#Matrix script
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)


# In[ ]:


#python:Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)


# In[ ]:


#Loop
def square(n):
  for i in range(0,n):
        print(i**2)
      
square(int(input()))


# In[ ]:


#write a function
def is_leap(year):
    leap = False
    if year % 4==0 and (year % 400 == 0 or year % 100 != 0):
          return True
    else:
          return False


# In[ ]:



#print function
def a(n):
      print(*range(1,int(input())+1),sep='')
 


# In[ ]:


#list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range (x+1) for j in range (y+1) for k in range(z+1) if i+j+k !=n])


# In[ ]:


#Find the Runner-Up Score!

n = int(input())
arr = set(map(int, input().split()))
arr.remove(max(arr))
print (max(arr))


# In[ ]:


#nested Lists
marksheet=[]
score_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet+= [[name,score]]
    score_list+=[score]

second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,marks in sorted(marksheet):
    if marks == second_lowest_mark:
        print(name)


# In[ ]:


#Lists
N = int(input())
l=[]
for n in range (N):
  x= input().split(" ")
  command= x[0]
  if command=="append":
    l.append(int(x[1]))
  if command=="print":
    print(l)
  if  command == "insert":
    l.insert(int(x[1]),int(x[2]))
  if command == "reverse":
    l.reverse()
  if command =="pop":
    l.pop()  
  if command =="sort":
    l.sort()
  if command == "remove":
    l.remove(int(x[1]))


# In[ ]:


#Tuples
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))


# In[ ]:


#sWAP cASE
def swap_case(s):
    swaped = ""
    for i in s:
        if i == i.upper():
            swaped += i.lower()
        else:
            swaped += i.upper()
    return swaped


# In[ ]:


#String split and join

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return(line)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


#What's Your Name?
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))


# In[ ]:


#Mutation
def mutate_string(string, position, character):
    return(string[:position] + character + string[position+1:])


# In[ ]:


#String Validator
S = input()
print(any (s.isalnum() for s in S))
print(any (s.isalpha()for s in S))
print(any (s.isdigit()for s in S))
print(any (s.islower()for s in S))
print(any (s.isupper() for s in S))  


# In[ ]:


#Text alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


#text wrap
def wrap(string, max_width):
    return(textwrap.fill(string,max_width))
    


# In[ ]:



#Designer Door mat
N, M = map(int, input().split()) 
for i in range(1,N,2): 
  print((i*'.|.').center(M,'-'))
print('WELCOME'.center(M,'-')) 
for i in range(N-2,-1,-2): 
    print((i*'.|.').center(M, '-'))


# In[ ]:


#Introduction to sets
def average(array):
    set_arr= set(arr)
    sum_arr=sum(set(arr))
    average= sum_arr/len(set_arr)
    return average


# In[ ]:


#No Idea!
n,m=map(int,input().split())
array_elem=input().split()
A=set(input().split())
B=set(input().split())
count_happiness=0

for i in array_elem:
    if i in A:
        count_happiness+= 1
    if i in B:
        count_happiness -= 1
print(count_happiness)


# In[ ]:


#set.add()
n=int(input())
country =set()
for i in  range (n):
  country.add(input())
print(len(country))


# In[ ]:


#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
a= int(input())
for i in range (a):
    m=input().split()
    if m[0] == "remove" :
        s.remove(int(m[1]))
    elif m[0] == "discard":
        s.discard(int(m[1]))
    elif m[0] =="pop":
        s.pop()
print(sum(s))


# In[ ]:


#Set .union() Operation
n=int(input())
eng=set(input().split())
b=int(input())
frn=set(input().split())
print(len(eng|frn))


# In[ ]:


#Set .intersection() Operation
n=int(input())
eng=set(input().split())
b=int(input())
frn=set(input().split())
print(len(eng&frn))


# In[ ]:


#Set .difference() Operation
n=int(input())
eng=set(input().split())
b=int(input())
frn=set(input().split())
print(len(set(eng- frn)))


# In[ ]:


#Set .symmetric_difference() Operation

n=int(input())
eng=set(input().split())
b=int(input())
frn=set(input().split())
print(len(set(eng^frn)))


# In[ ]:


#Set Mutations

n = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for n in range(N):
    m = input().split()
    s2 = set(map(int, input().split()))
    if(m[0] == "intersection_update"):
        s1.intersection_update(s2)
    elif(m[0] == "update"):
        s1.update(s2)
    elif(m[0] == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(m[0] == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))


# In[ ]:


#collections.Counter()
import collections

shoes_num= int(input())
shoes = collections.Counter(map(int,input().split()))
n= int(input())

result = 0

for i in range(n):
    size, price = map(int,input().split())
    if shoes[size]: 
        result += price
        shoes[size] -= 1

print (result)


# In[ ]:


#Calendar Module
import calendar
MMDDYYYY=list(map(int,input().split()))
weekday=calendar.weekday(MMDDYYYY[2],MMDDYYYY[0],MMDDYYYY[1])
if weekday==0:
    print("MONDAY")
if weekday==1:
    print("TUESDAY")
if weekday==2:
    print("WEDNESDAY")
if weekday==3:
    print("THURSDAY")
if weekday==4:
    print("FRIDAY")
if weekday==5:
    print("SATURDAY")
if weekday==6:
    print("SUNDAY")  


# In[ ]:


#Exceptions
T=int(input())
for i in range(T):
    try:
        a,b=input().split()
        print (int(a)//int(b)) #integer division
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


# In[ ]:


#Zipped
n, x = map(int, input().split())
l=[]
for i in range(x):
    l.append(list(map(float, input().split())))
print(*[sum(s)/len(s) for s in zip(*l)],sep='\n')


# In[ ]:


#map and lambda function
cube = lambda x: x**3
def fibonacci(n):
    # return a list of fibonacci numbers
    l=[]
    if n==0:
        return l
    elif n==1:
        return [0]
    else:        
     a=0
     b=1
     l.append(a)
     l.append(b)
     for i in range(n-2):
        c=a+b
        a=b
        b=c
        l.append(c)
     return l  


# In[ ]:


#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l] #making output format (adding the +91 and putting the spaces
        return f(decorated_l)
    return fun


# In[ ]:


#Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))] #sorting based on the third item x[2] in each line of input
    return inner


# In[ ]:


#Arrays
def arrays(arr):
    return(numpy.array(arr[::-1], float))
#arr[::-1] makes arr reveresed.
#numpy.array(, float) makes arr an array with float members.


# In[ ]:


#Shape and Reshape
import numpy

# 3 steps as follows:
#   read a list as input
#   convert it ro numpy array
#    reshaoe it to 3x3 array

a = list(map(int,input().strip().split()))
my_array = numpy.array(a)
print(numpy.reshape(my_array,(3,3)))


# In[ ]:


#Transpose and Flatten
import numpy

# 4 steps of Code are as follows:
    # Reading a list of inputs
    # converting the list to a numpy array
    # Transpose the array
    # fallten the array


N, M = input().split()
a= []
for i in range(int(N)):
    b = input().split()
    a.append(b)
m_array = numpy.array(a, int)
print (numpy.transpose(m_array))
print (m_array.flatten())


# In[ ]:


#Concatenate
import numpy as np

#Steps are as follow:
    # Reading inputs as N, M and P
    # Creating a list (l) and putting all digits in it
    # converting it to a numpy array

N,M,P=map(int,input().split())
l=[]
for i in range(N+M):
    b=input().split()
    l.append(b)
print(np.array(l,int))


# In[ ]:


#Zeros and Ones

import numpy

# Steps are as follow:
#   Reading dimension(s) of array as a list
#   printing arrays based on specified dimensions

a = list(map(int, input().split()))
print (numpy.zeros((a), dtype = numpy.int))
print (numpy.ones((a), dtype = numpy.int))


# In[ ]:


#Eye and Identity
import numpy

#Steps are as follow:
    # Receiving inputs
    # creating EYE
    # correcting spaces in result as excersice asked 



n,m = map(int,input().split())
a = numpy.eye(n,m)
print(str(a).replace('1',' 1').replace('0',' 0'))


# In[ ]:


#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    return(ar.count(max(ar)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Kangaroo
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    k=1
    if v2>=v1:
        return "NO"
    
    while (x2+(k*v2)>= x1+(k*v1)):
        if x2+(k*v2) == x1+(k*v1):
            return "YES"
        k +=1
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    seead = 5
    likad = 0
    cum = 0
    for i in range(0, n):
        likad = seead//2
        cum += likad
        seead = likad * 3
    return (cum)
    for i in range(0, n):
        likad = seead//2
        cum += likad
        seead = likad * 3
    return (cum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    j=10
    l=[]
    if len(n)>1:
        while (int(n)!=0):
            a=int(n)%10
            l.append(a)
            n=int(n)//10
        f=sum(l)*k
        return(superDigit(str(f),1))
    if len(n)==1:
        return n



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    a = arr[n-1]                                                 
    for i in range(n-2):
        if arr[n-i-2]>a:
            arr[n-i-1]= arr[n-i-2]
            print(*arr, sep=' ')
        else:
            arr[n-i-1] = a
            print(*arr, sep=' ')
            break
    if arr[1] > a:
        if arr[0] >a:
            arr[1] = arr[0]
            print(*arr, sep=' ')
            arr[0]=a
            print(*arr, sep=' ')
        else:
            arr[1] = a
            print(*arr, sep=' ')
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# In[ ]:


#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        for a in range(i+1):
            if arr[a] >= arr[i]:
                c=arr[i]
                for b in range(i+1-a):
                    arr[i-b]=arr[i-b-1]
                arr[a]=c
                print(' '.join(str(x) for x in arr))
                break
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

