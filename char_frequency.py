
text = input("Enter a string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

for char, count in freq.items():
    print(f"{char}: {count}")

 
