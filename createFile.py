nama = []
npm = []
print("===============TUGAS STRUKDAT===============")
jml_data = int(input("Masukan Jumlah data : "))

for i in range(jml_data):
    i+=1
    print("===========Data Mahasiswa ke -",i,"===========")
    nm = str(input("Masukan Nama    : "))
    np = (input("Masukan NPM     : "))
    print("===========================================")
    nama.append(nm)
    npm.append(np)
    
with open('nama.txt', 'w') as fnama:
    for line in nama:
        fnama.write(f"{line}\n")
fnama.close()
with open('npm.txt', 'w') as fnpm:
    for line in npm:
        fnpm.write(f"{line}\n")
fnpm.close()