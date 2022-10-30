list1 = [2, 5, 3]
list2 = [3, 2, 1]
list3 = []
list4 = []
for x in list2:
    for i in list1:
        #mult = x * y
        list3.append(x * i)
for i in range(len(list1)):
        list4.append(list1[i] * list2[i])
print(list3+list4)


