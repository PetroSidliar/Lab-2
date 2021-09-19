import math

inp = input()
print(bool(inp))
if inp is None:
    print('Input is none')
elif math.isnan(inp):
    print('Input is Nan')
