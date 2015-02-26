#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("013.txt", "r")
print(str(sum([int(x.strip()) for x in f]))[:10])
f.close()
