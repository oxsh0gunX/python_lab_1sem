list1 = list(map(int, input("Enter first list of integers: ").split()))
list2 = list(map(int, input("Enter second list of integers: ").split()))

if len(list1) == len(list2):
    print("Both lists are of the same length")
else:
    print("Lists are of different lengths")

if sum(list1) == sum(list2):
    print("Both lists have the same sum")
else:
    print("Lists have different sums")
