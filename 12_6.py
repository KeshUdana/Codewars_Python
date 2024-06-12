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