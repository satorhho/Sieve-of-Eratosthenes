upperbound = int(input("Upper bound:  "))
A = [i for i in range(2, upperbound + 1)]

size = upperbound - 1
i = 0
while i < size:
    denominator = A[i]
    j = i +1
    while (j < size):
        if not (A[j] % denominator):
            A.pop(j)
            size -= 1
        else:
            j += 1
    i += 1

print(A)