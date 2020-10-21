def bitwiseComplement(n):
    if n == 0:
        return 1
    sol = 0
    count = 0
    while n > 0:
        if n%2 == 0:
            sol += 2 ** count
        n = n // 2
        count += 1
    return sol


def toBinary(num):
    if num>1:
        toBinary(num // 2)
        print(num%2)



num = 24
print(bitwiseComplement(num))