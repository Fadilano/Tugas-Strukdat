"""
Pada line 5-9 disini adalah pendeklarasian variable yang digunakan dan judul dari program ini, Setelah itu pada line ke 10 buat perintah 
untuk user memasukkan jumlah data yang diiinginkan dan nilai ini akan disimpan sebagai nilai dari variable jml_data
"""
nama = []
npm = []                
kelas = [] 
jurusan = []                                                     
print("===============TUGAS STRUKDAT===============")
jml_data = int(input("Masukan Jumlah data : "))
"""
Selanjutnya masuk kepada perulangan pada program ini, perulangannya ditentukan dari berapa jumlah data yang diinginkan user tadi yang disimpan 
pada variable jml_data tadi. Maka untuk kondisi fornya bisa menggunakan kondisi 
for i in range(jml_data):
    i+=1 
Dan perulangannya berisi tentang perintah ntuk uuser menginputkan data data yang dimasukkan nantinya yaitu sesuuai variabel diatas tadi yaitu
Nama, Kelas, NPM, Dan Jurusan. 
"""
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
