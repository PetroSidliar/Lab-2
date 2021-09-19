example = [[1, 'a'],  [3, 'c'],  [5, 'c'], [2, 'b'], [4, 'd']]


def func(mylist=[], numflag=False):
    if numflag == False:
        return sorted(mylist, key=lambda el: el[1])
    else:
        return sorted(mylist, key=lambda el: el[0])
    

print(func(example))
print(func(example, numflag=True))
