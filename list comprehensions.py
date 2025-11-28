#sreehari c
#a)generate positive list of numbers from a given list of integers.

main_list = [ -2, -9, 0, 7, -6, 88, -23, 84]
posi_list = []

list_size = int(input("Enter the size of the list : "))
main_list = []
posi_list = []

for i in range (list_size):
    value = int(input(f"Enter element {i + 1}: "))
    main_list.append(value)

for i in range (len(main_list)):
    if main_list[i] > 0:
        posi_list.append(main_list[i])

print ("The positive numers are : ", posi_list)

#b) square of N number

N = int(input("Enter the value of N : "))
square_list = []

for i in range (N+1):
    square_list.append(i**2)

print(f"The list of {N} square are : " , square_list)


#c)form a list of vowels selected from given word

word = str(input("Enter a word or sentence : "))

vowels = [ "a", "e", "i", "o", "u" , "A" , "E" , "I" , "O" , "U"]

vowel_list = []

for i in range(len(word)):
    if word[i] in vowels:
        vowel_list.append(word[i])

print("The list of wovels in the word or sentance is : " , vowel_list)


#c)OR

word = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
vowel_list = []

for char in word:
    if char in vowels:
        vowel_list.append(char)

print("List of vowels in the input:", vowel_list)


#d)list ordinal values of each element of a word

ordinals = []
word = "Happy"
for ch in word:
    ordinals.append(ord(ch))

print ("the ordinal values are : " , ordinals)
