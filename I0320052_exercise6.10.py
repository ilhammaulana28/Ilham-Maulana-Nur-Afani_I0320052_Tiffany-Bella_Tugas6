print('Exercise 6.10')
i = 1
while i < 10:
    j = 1
    while j < i:
        print('%d' % (i*j), end='')
        j = j + 1
    print()
    i = i + 1