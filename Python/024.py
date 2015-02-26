from itertools import permutations
x = ["".join(item) for item in permutations("0123456789")]
x.sort()
print(x[999999])
