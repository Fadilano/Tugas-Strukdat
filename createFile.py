nama = []
npm = []
kelas = []
jurusan = []
print("===============TUGAS STRUKDAT===============")
jml_data = int(input("Masukan Jumlah data : "))

for i in range(jml_data):
    i+=1
    print("===========Data Mahasiswa ke -",i,"===========")
    nm = str(input("Masukan Nama    : "))
    np = (input("Masukan NPM     : "))
    kls = (input("Masukan Kelas   : "))
    jrsn = (input("Masukan Jurusan : "))
    print("===========================================")
    nama.append(nm)
    npm.append(np)
    kelas.append(kls)
    jurusan.append(jrsn)
    
with open('nama.txt', 'w') as fnama:
    for line in nama:
        fnama.write(f"{line}\n")
fnama.close()
with open('npm.txt', 'w') as fnpm:
    for line in npm:
        fnpm.write(f"{line}\n")
fnpm.close()
with open('kelas.txt', 'w') as fkelas:
    for line in kelas:
        fkelas.write(f"{line}\n")
fkelas.close()
with open('jurusan.txt', 'w') as fjurusan:
    for line in jurusan:
        fjurusan.write(f"{line}\n")
fjurusan.close()
