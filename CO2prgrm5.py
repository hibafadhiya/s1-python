def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
num = 36
print(f"Factors of {num} are: {factors(num)}")
