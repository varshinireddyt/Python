"""
1.3 : URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has
 space at the end to hold the additional characters,and that you are given the "true" length of the string.
 Time Complexity: O(n)
"""

def replaceSpace(str):
    for i in range(len(str)):
        if str[i] == " ":
            str = str[:i] + "%20" + str[i+1:]
    return str

str = "Mr John Smith"
print(replaceSpace(str))