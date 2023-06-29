#in this case the problem is given an integer x, return "true" if x is a palindrome. "false" otherwise
#for submitting just copy the code to leetcode and erase the variable x, for it's the argument of the method of the class solution in the page

x = 123
y = x
pal = 0
while x > 0:
    digit = x % 10 
    pal = pal * 10 + digit
    x = x // 10
    

    
