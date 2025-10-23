
n = int(input("Enter the number of terms: "))

a, b = 0, 1
series = []

for _ in range(n):
    series.append(a)
    a, b = b, a + b

print("Fibonacci series:", series)

