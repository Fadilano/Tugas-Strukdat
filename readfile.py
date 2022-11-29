fnama = open("nama.txt", "r")
fnpm = open("npm.txt", "r")

readnama = fnama.readlines()
readnpm = fnpm.readlines()

print("""
+--------------------+-------------------+
| NAMA               | NPM               |
+--------------------+-------------------+
""")

for i in range (len(readnama)):
    nama = str(readnama[i].strip())
    print('| '+nama,end='')
    for j in range(20-1-len(nama)):
        print(' ',end ='')
    npm = str(readnpm[i].strip())
    print('| '+npm,end='')
    for k in range(19-1-len(npm)):
         print(' ',end ='')
    
    print('|')

print("+--------------------+-------------------+")
