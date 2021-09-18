def is_sorted(l):
    return l == sorted(l)

example1 = [1, 2, 3, 4]
example2 = [1, 2, 4, 3]

print(is_sorted(example1))
print(is_sorted(example2))
