#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these
#values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
#is a triangle number then we shall call the word a triangle word.
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
#English words, how many are triangle words?

f = open("042.txt", "r")
words = [line.strip().split(",") for line in f][0]
f.close()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

l = []
for word in words:
    total = 0
    for letter in word:
        if letter in alphabet:
            total += alphabet.index(letter) + 1
    l.append(total)

tri = [1]
n = 1
while tri[-1] < max(l):
    tri.append(int(.5 * n * (n + 1)))
    n += 1

count = 0
for score in l:
    if score in tri:
        count += 1
print(count)
