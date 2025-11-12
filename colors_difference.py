
list1 = input("Enter colors for list1 (comma-separated): ").split(',')
list2 = input("Enter colors for list2 (comma-separated): ").split(',')

list1 = [color.strip() for color in list1]
list2 = [color.strip() for color in list2]

diff = [color for color in list1 if color not in list2]

print("Colors in list1 not in list2:", diff)
 
