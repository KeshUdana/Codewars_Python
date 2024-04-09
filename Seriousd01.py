for i in range(2,101):
    if i%2!=0 or 1 and i%3!=0 or 1:
        print(i," is a prime number")
.......................................................................
l1 = ["red", "green", "yellow", "black"]
l2 = ["red", "purple", "pink", "green"]
comm_char=[]
for i in l1:
    if i in l2:
        comm_char.append(i)
        
print(comm_char," is present in both list 1 and list 2")
.........................................................................
import random

l1=[random.randint(1,101) for i in range (1,101)]
print(l1[:20])
............................................................................
for i in range(1,101):
    if i%2==0:
        print(i)
................................................................................
for i in range(1,101):
    if i%2!=0:
        print(i)
.....................................................................................
import random
l1=[random.randint(0,101) for i in range (1,101)]
l2=l1[:20]
if len(l2)==20:
 print("YES")
for i in l2:
    if i%2==0:
        print(i," is an even number")
...............................................................................................
#Generate a list of 20 random numbers and calculate their sum.
import random
l1=[random.randint(0,101) for i in range (0,20)]
print(sum(l1))

.......................................................................................................
#Write a function to identify and print all even numbers from a given list.
def get_even(x):
    res=[]
    for i in x:
        if i%2==0:
            res.append(i)
    return res

l1=[1,2,44,54,66,42,100000,1022]
print(get_even(l1))
.....................................................................................................................
#Write a Python program to calculate the factorial of a given number.
count=0
xlist=[]
while True:
    x=int(input("Enter number: "))
    xlist.append(x)
    count+=1
    if count==3:
        break
        x=1
for i in xlist:
    x=x*i
print(x)
..............................................................................................................................
#Create a function that takes a sentence as input and counts the occurrences of each word. Print the word frequency.


...............................................................................................................................
#Given a list of numbers, write a program to find the second largest number in the list.
numlist=[]
while True:
    num=float(input("Enter number: "))
    numlist.append(num)
    ques=input("Do you want to enter another number, press any key, else type no".lower())
    print(ques)
    if ques!="no":
        continue
    else:
        break
    descending_list=sorted(numlist, reverse=True)
print("the second highest is: ",descending_list[1])
....................................................................................................................................
#Implement a function that checks if a given string is a palindrome (reads the same backward as forward).
word1=list(input("Enter word: "))
word2=word1[::-1]
if word1==word2:
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")
......................................................................................................................................................................................................
#Create a dictionary with student names and their corresponding average scores. Print the student with the highest average.
name=input("Enter student names: ").split(",")
ave=input("Enter student averages: ").split(",")
dict_1={}
for n,a in zip(name,ave):
    dict_1[n]=int(a)
print(dict_1)
"""In this example, zip(names, averages) is used to pair up the names and averages,
and then a dictionary is created where the names are the keys,
and the averages are the values."""
............................................................................................................................................................................................................
#Write a Python function to check if a given year is a leap year.
def check_year():
    year=int(input("Enter you year: "))
    if year%4==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
    return

check_year()
...............................................................................................................................................................................................................
#Given a list of integers, write a Python program to find the sum of all the positive numbers in the list.
pos_list=[]
nums=input("Enter integers: ")
num_list=[int(i)for i in nums.split(",")]
for i in num_list:
    if i>=0:
        pos_list.append(i)
print(sum(pos_list))
.............................................................................................................................................................
#Implement a program that takes a sentence as input and prints the words in reverse order.
sen_list=sen.split()
new_list=sen_list[::-1]
print(new_list)

sen=input("Enter your sentence: ")
sen_list=sen.split()
new_list=sen_list[::-1]
print(new_list)
................................................................................................................................................................
#Remove duplicate elements from a list.
list1 = input("Enter characters: ").split(",")
set1 = set(list1)
print("Duplicates have been removed:", set1)
.............................................................................................................................................................
#find square root of a number
num=float(input("Enter number: "))
print(num**0.5)
............................................................................................................................................................
#Create a function to check if a given number is prime.
num=int(input("Enter number: "))
if num>1 and  num==2 or num==3 or (num%2!=0 and num%3!=0):
    print(num," is a prime number")
else:
    print(num,"is NOT a prime number")
..................................................................................................................................................................
import random

n=10**10000000000
num = input("Enter numbers: ")
num_list = [int(i)for i in num.split(",")]

ran_num = [random.randint(0, n) for _ in range(len(num_list))]

unique_num = [i for i in num_list if i not in ran_num]

print("Following numbers are NOT common to both of them: ", unique_num)
print("Generated random numbers: ", ran_num)
....................................................................................................................................................................
import random
expo=random.randint(0,10);num=float(input("Enter number: "))
print(num**expo," is the result")
#..................................................................................................................................................................
#Write a Python function that takes a list of numbers as input and returns a new list with only the even numbers from the original list, doubled.
num=input("Enter numbers: ")
num_list=[int(i)for i in num.split(",")]
eve_list=[]
for i in num_list:
    if i%2==0:
        i*=2
        eve_list.append(i)
    else:
        pass
    
print(eve_list)
#........................................................................................................................................................................................................................................................................................................................
l1=[]
for i in range (25,96):
    if i%3==0:
        l1.append(i)
    else:
        pass
print(l1)
#.......................................................
#reverse  astring and print it without spaces
s1="Hello world im here"
rev=list(reversed(s1))
for i in rev:
    if " " in rev:
        rev.remove(" ")
print(rev)
........................................................................................
#Print each character of a string on a separate line. and reverse it

st1="Hello"
ls1=list(reversed(st1))
for i in ls1:
    print(i)
...................................................................................................................................................................................................................................................................................................
#Count the number of vowels in a string.
count=0
st1="Hello world, im here"
for i in st1:
    if i=="a" or i=="e" or i=="i"or i=="o"or i=="u":
        count+=1
print(count)
............................................................................................................................................................................................................................................................................................................
#check if string is palindrome
s1=input("Enter word: ")
l1=list(s1)
print(l1)
l2=l1[::-1]
print(l2)
if l1==l2:
    print(s1," is a palindrome")
else:
    print(s1,"is not a palindrome")
....................................................................................................................................................
#Given a list of movie ratings, sort them from highest to lowest and print the top 5 rated movies.
mov_rat= [4.5, 3.8, 2.5, 4.0, 3.2, 5.0, 4.7, 3.5, 2.8, 4.2]
sorted_mov_rat=sorted(mov_rat)
print(sorted_mov_rat)
print(sorted_mov_rat[-5:])




































