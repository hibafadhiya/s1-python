N = int(input("Enter the number of terms: "))
a, b = 0, 1
if N <= 0:
    print("Please enter a positive integer.")
elif N == 1:
    print("Fibonacci series up to 1 term:")
    print(a)
else:
    print(f"Fibonacci series up to {N} terms:")
    print(a, b, end=' ')
    for _ in range(2, N):
        c = a + b
        print(c, end=' ')
        a, b = b, c
