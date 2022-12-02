"""
dibawah ini terdapat proses inisialisasi pembacaan file kedalam variabel lain
sebagai contoh fnama berisi data-data dari file nama.txt yang telah dibaca
dengan fungsi "r"
"""
fnama = open("nama.txt", "r")
fnpm = open("npm.txt", "r")
fkelas = open("kelas.txt", "r")
fjurusan = open("jurusan.txt", "r")

readnama = fnama.readlines()
readnpm = fnpm.readlines()
readkelas = fkelas.readlines()
readjurusan = fjurusan.readlines()
#Line 11-14 ini fungsinya sebagai membaca file txt nya berupa string
print("""
+--------------------+-----------------+-----------+---------------+
| NAMA               | NPM             |KELAS      |JURUSAN        |
+--------------------+-----------------+-----------+---------------+""")
# Kemudian Membuat tabel dengan Print di design seperti code diatas.
for i in range (len(readnama)):
    nama = str(readnama[i].strip())
    print('| '+nama,end='')
    #perulangan for dengan variabel i in range atau dalam jarak seberapa panjang, variabel nama tersebut
    #dan variabel nama = string readnama yang dimasukkan variabel i perulangannya dan strip sebagai menghasilkan karakternya besar atau kecil
    #kemudian cetak +nama,end='' artinya mencetak dengan membuat baris baru ketika mencetak lagi.
    for j in range(20-1-len(nama)):
        print(' ',end ='')
    npm = str(readnpm[i].strip())
    print('| '+npm,end='')
    for k in range(17-1-len(npm)):
         print(' ',end ='')
    kelas = str(readkelas[i].strip())
    print('| '+kelas,end='')
    for p in range(11-1-len(kelas)):
         print(' ',end ='')
    jurusan = str(readjurusan[i].strip())
    print('| '+jurusan,end='')
    for v in range(15-1-len(jurusan)):
         print(' ',end ='')
    #selanjutnya masih sama seperti tadi perulangan for dengan variabel j, k, p, v dalam jarak 20-1-len dan 19-1-len dimasukkan variabel nya masing masing disesuaikan
    #mencetak dengan print untuk baris barunya dan npm = string readnpm yang dimasukkan variabel i perulangannya dan strip sebagai menghasilkan karakternya besar atau kecil
    #lalu cetak lagi dengan akhiran end=
    
    print('|')
    #sebagai penutup dari tabel outputan

print("+--------------------+-----------------+-----------+---------------+")
#sebagai bagian bawah dari tabel
