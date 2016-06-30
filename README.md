# Leetcode-solutions
thoughts and solutions to Leetcode problems

#Reverse Integer
Firstly convert Integer to String: s=str(i)
Then use Python inbulit method to reverse a string: [::-1]
Then conver String to Integer: i=int(s)
Note that Python has a default range for Int type: -2147483647 to 2147483647, so if the original int value or reversed value falls out of this range, 0 should be returned

#Zig Zag Conversion
The zigzag pattern is:
a    g   m
b  f h  l
c e  i k
d    j

So the returned string should read from the first row, then second row, ...
Construct a Python dictionary: d={}
Store each row as a record to the dict
The normal element stored should be i%(d*numOfRows-2)=k, where k=1 to numOfRows
When k>=numOfRows, correspond to the element in the middle, the stored position should be (numOfRows-1)-(i-(numOfRows-1))
