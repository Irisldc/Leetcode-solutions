# Leetcode-solutions
thoughts and solutions to Leetcode problems

#Reverse Integer & Palindrome Number
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

#longest common prefix
the longest common prefix length will not exceed the shortest string length in the list, thus we need to find the shortest string in the list. the python inbuilt method min(list, key=len) can be used.
Then we can loop from the first to last character of the shortest string and check if each string in the list has the same character in the same position. If any string does not contain the character, the longest common prefix will be the last one
Note that we should consider the empty list situation, to check if a list is empty, if not list:... can be used

#Remove Nth Node From End of List
the input type was defined as a linked list, where 1->2->3->4
each element in the linked list is a ListNode, the ListNode class has two operations, node.val returns the value of the current node, and node.next returns the linkedlist after the current node

The first thing to do is to assign each node value of a linkedlist to a normal list: l=[]. To traverse a linked list, the node.next and node.val function should be used: while current_node != None then l.append(current_node.val) and current_node=linked_list.next

The second step is to reverse the list l and delete element from the start: l=[::-1], l=[:n-1]+l[n:]

The last step is to reconstruct a linked list according to the list value. Note that the initialization of a ListNode is ln=ListNode(value). The most important thing of this step is that, the fist node to put into the LinkedList will become the last element to read, as one can only assign the current value to a node, and the previews linkedlist will be assigned as the next to the current node.

#Valid Parentheses
determine whether a input string has valid parentheses, (){}[] can be adjacent or nested such as [{}]()
Then can use python inbuilt method str.replace('()','') to remove all adjacent pair of (){}[], until the orginal string contains no more (){}[] pair. Then if the remaining string is empty, the input is valid

#implement strStr() function
strStr(str1, str2) function determine whether str2 is a substring of str1, if yes, the function returns the first index of str2, if not, returns -1
My thought is to firstly convert the string of str1 into a dictionary, use the position as key and character as value, since the search of dic is n times faster than a list.
I used if str2 in str1 to determine whether str2 is in str1, if not, returns -1
Then I loop from the string str1 to find each substring the same length as str2, if there is a substring aquals to str2, return the index of the key.
Note that if str2 is empty, 0 should be returned.
