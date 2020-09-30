"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

1 - 10  4, 9
10 - 50, 50 -100
100 - 500, 500 - 1000
"""
def intToRoman(num):
    ones = ["",'I','II','III','IV','V','VI','VII','VIII','IX']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXX','XC']
    hundreds = ['','C','CC','CCC','DC','D','DC','DCC','DCCC','CM']
    thousands = ['','M','MM','MMM']
    return thousands[num//1000]+hundreds[num%1000 //100]+tens[num%100 //10]+ones[num%10]



num = 45
print(intToRoman(num))

