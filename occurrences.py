text = input("Enter a line of text: ")
words = text.split()
word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1
for word, count in word_count.items():
    print(f"{word}: {count}")
