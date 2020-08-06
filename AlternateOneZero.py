def solution(A):
    count = 0
    temp_bit = A[0]
    for i in range(1, len(A)):
        if (temp_bit == A[i]):
            count = count + 1
        if (temp_bit == 0):
            temp_bit = 1
        elif (temp_bit == 1):
            temp_bit = 0

    count_2 = 1
    temp_bit = A[0]
    if (temp_bit == 0):
        temp_bit = 1
    elif (temp_bit == 1):
        temp_bit = 0
    for i in range(1, len(A)):
        if (temp_bit == A[i]):
            count_2 = count_2 + 1
        if (temp_bit == 0):
            temp_bit = 1
        elif (temp_bit == 1):
            temp_bit = 0
    return min(count, count_2)

A = [1,1,0,1,1]
print(solution(A))