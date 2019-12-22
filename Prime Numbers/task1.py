
numbers = list(range(0, 10 ** 7, 1))
prnum = []
for i in numbers[2:]:
    if i != 0:
        for c in range(2 * i, len(numbers), i):
            numbers[c] = 0
for k in numbers:
    if k != 0:
        prnum.append(k)
with open('primenumbers.txt', 'w') as file:
    for a in prnum[1:]:
        file.write('%s\n' % a)
