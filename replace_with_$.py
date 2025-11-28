#7/8)get string from user input. replace each inputs first letter with '$'

text = input(str("Etere : "))

word = list(text)
result = word[0]

for i in word[1:]:
    if i != word[0]:
        result += i
    else:
        result += "$"

print("Result : " , result)

