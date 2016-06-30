# Leetcode-solutions
thoughts and solutions to Leetcode problems

Reverse Integer
Firstly convert Integer to String: s=str(i)
Then use Python inbulit method to reverse a string: [::-1]
Then conver String to Integer: i=int(s)
Note that Python has a default range for Int type: -2147483647 to 2147483647, so if the original int value or reversed value falls out of this range, 0 should be returned
