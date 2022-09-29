# define palindrome
# create a empty string
# for i in s then
# if i is >='a'and i is <='z'
# a equals a + i
# if i is >='a'and i is <='z'
# a equals a + i.lower()
#Since we have traversed string s only once hence time complexity is O(n) 
# Time complexity: O(n) 
#'''.lower() function is used to convert uppercase characters to lowercase
#a[::-1] returns the reversed string.
#Hence comparing if string and reverse string is same or not.'''



def palindrome(s):
    a = ""
    for i in s:
        if i >= 'a' and i <= 'z':
            a = a + i
        if i >= 'A' and i <= 'Z':
            a = a + i.lower()
        
    if a == a[::-1]:
        return True
    return False


s = input("Enter a string ")
if (palindrome(s)):
    print("Palindrome")
else:
    print("Not palindrome")

