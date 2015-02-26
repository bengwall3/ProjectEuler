#What is the first term in the Fibonacci sequence to contain 1000 digits?

f = [1, 1]
n = 2
while len(str(f[-1])) < 1000:
    f = [f[-1], f[-2] + f[-1]]
    n += 1
print(n, f[-1])
