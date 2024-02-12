#Python membership and identy operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for a in list1:
    if a in list2:
        print("overlapping")
    else:
        print("not overlapping")