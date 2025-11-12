str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > 1 and len(str2) > 1:
    str1, str2 = str2[0] + str1[1:], str1[0] + str2[1:]

result = str1 + " " + str2
print("Resulting string:", result)
   
