"""The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""

a = int(input())
b = int(input())
print(a//b)
print(a/b)

"""Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line."""
n = int(input())
x=0
while n>0 and n!=x:
    y=x*x
    x=x+1
    print(y)

"""Given a year, determine whether it is a leap year. 
If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
It is only necessary to complete the is_leap function."""
def is_leap(year):
    leap = False
    if 1900 <= year <= 100000:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            leap = True
    return leap

year = int(input())
print(is_leap(year))

"""The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between
Print the list of integers from  through  as a string, without spaces."""
n = int(input())
x=1
while x<=n and 1<=n<=150:
    print(x,end='')
    x=x+1
