numbers = input("Enter integers separated by spaces: ").split()
result = []
for n in numbers:
    n = int(n)
    if n > 100:
        result.append("over")
    else:
        result.append(n)
print(result) 
