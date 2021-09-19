lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) # adding the element
     
print(lst)
print('Total number of items in the list:', len(lst))
last_element = lst[-1]
print('Last element:' , last_element)
lst.reverse()
print('Reversed List:', lst)
if (5 in lst) :
    print("YES")
else:
    print("NO")
print(lst.count(5))
lst.pop(0)
lst.pop()
lst.sort()
print(lst)
print(len([1 for i in lst if i > 5]))

