fnama = open("nama.txt", "r")
fnpm = open("npm.txt", "r")
fkelas = open("kelas.txt", "r")
fjurusan = open("jurusan.txt", "r")

readnama = fnama.readlines()
readnpm = fnpm.readlines()
readkelas = fkelas.readlines()
readjurusan = fjurusan.readlines()

print("""
+--------------------+-----------------+-----------+---------------+
| NAMA               | NPM             |KELAS      |JURUSAN        |
+--------------------+-----------------+-----------+---------------+""")

for i in range (len(readnama)):
    nama = str(readnama[i].strip())
    print('| '+nama,end='')
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
    
    print('|')

print("+--------------------+-----------------+-----------+---------------+")
