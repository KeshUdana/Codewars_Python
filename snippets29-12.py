'''Python excercise questions and codes  to practice for viva

1.Find the length of a string
 eg="Random words"

2.To find if a certain character is present in a string
3.Print ("Yes") if a certain character is present in a string
4.Loop through the items in a list:
    fruits=["apples","orange","banana","mango"]
    veg=["carrots","leeks","ginger","spinach"]
    for i in fruits:
        print(i,"is a fruit")
        continue 
    for i in veg:
        print(i,"is a vegetable")

5.Use of pop method
  car={"brand":"Toyota","model":"Prius","year":"2020"}
    print(car.pop("model"))
    
6.Use insert in lists:
 alphabet=['a','b','c','e']
 print(alphabet.insert(3,'d'))
 
 7Using insert method
 alphabet=['a','b','c','e']
print(alphabet.insert(3,'d'))
print(alphabet)

8.alphabet=['a','b','c','e']
(alphabet.insert(3,'d'));print(alphabet)
.................................................................
9.Given an integral number, determine if it's a square number:
OP should be like this:
def basic_test_cases():
        test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
        test.assert_equals(is_square( 3), False, "3 is not a square number")
        test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
        test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
        test.assert_equals(is_square(26), False, "26 is not a square number")

Ans code:
import math

def is_square(n):
    try:
        if math.sqrt(n)**2 == n:
            print(n, "Is a square number")
            return True
        else:
            print(n, "Is not a square number")
            return False
    except ValueError:
        print("Error: Negative numbers cannot be square numbers")
        return False

# Example usage:
print(is_square(25))
 Best code i found for this:
 
 import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
.....................................................................................



