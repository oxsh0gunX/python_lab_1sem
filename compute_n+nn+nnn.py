#14) accept an integer n and calculate value of n+nn+nnn

n = float(input("Enter a integer : "))

total = n + (n*n) + (n*n*n)

print("The value is : " , total)