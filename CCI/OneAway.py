"""
Solution 1.5: There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

Using Minimum Edit Distance(Dynamic Programing)
credits: https://www.youtube.com/watch?v=b6AGUjqIPsA
"""
def editDistance(str1,str2,m,n):

    dp_table = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                dp_table[i][j] = 0
            elif i == 0:
                dp_table[i][j] == dp_table[i][j-1] + 1
            elif j == 0:
                dp_table[i][j] == dp_table[i-1][j] + 1
            elif str1[i-1] == str2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
            else:
                dp_table[i][j] = 1 + min(dp_table[i][j-1], dp_table[i-1][j], dp_table[i-1][j-1])
                #min(insert,remove,replace)
    return dp_table[m][n]



def oneAway(str1,str2):
    m = len(str1)
    n = len(str2)
    # return editDistance(str1,str2,m,n)
    if editDistance(str1,str2,m,n) == 1:
        return True
    else:
        return False

str1 = 'horse'
str2 = 'ros'
# print(oneAway(str1,str2))
print(editDistance(str1,str2))



