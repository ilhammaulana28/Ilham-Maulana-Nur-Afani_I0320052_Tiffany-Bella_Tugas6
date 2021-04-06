print('Exercise 6.13')
def tambah(a, b):
    c = a + b
    return c
x = int(input('Masukkan bilangan ke 1: '))
y = int(input('Masukkan bilangan ke 2: '))

hasil = tambah(x, y)
print('%d + %d = %d' % (x, y, hasil))