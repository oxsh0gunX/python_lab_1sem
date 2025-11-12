
text = input("Enter a string: ")
if len(text) > 1:
    result = text[-1] + text[1:-1] + text[0]
else:
    result = text
print(result)
  
