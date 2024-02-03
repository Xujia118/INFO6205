def FibI(n):
    a, b = 1, 1

    for _ in range(n - 2):
        temp = b
        b = a + b
        a = temp
    
    return b
    
print(FibI(10))