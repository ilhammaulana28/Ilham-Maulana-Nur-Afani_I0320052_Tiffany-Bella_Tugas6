print('Soal 2')
# program menghitung nilai rata2 dari nilai yang diinput user
# pengulangan for atau while
jumlah = int(input('Masukkan jumlah data yang akan diinput : '))
nilai = []
total = 0
for i in range(0, jumlah):
    i = i + 1
    tambah_nilai = int(input('Masukkan data ke-%d : ' % i))
    nilai.append(tambah_nilai)
print('\nData : ', nilai)
check = str(input('\nApakah data sudah benar (iya/tidak)?'))
if check == 'iya':
    for each in nilai:
        total = total + each
    print('\nRataan nilai anda adalah', total / jumlah)
else:
    input('\nSilahkan ulangi program!')
