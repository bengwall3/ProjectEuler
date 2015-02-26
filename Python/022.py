#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

f = open("022.txt", "r")
names = []
for line in f:
    for name in line.strip().split(","):
        names.append(name[1:-1])
f.close()
names.sort()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

def score(name):
    x = names.index(name) + 1
    y = sum([alphabet.index(letter) + 1 for letter in name])
    return x * y

for name in names:
    total += score(name)

print(total)
