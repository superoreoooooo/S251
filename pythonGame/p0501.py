import os

file = open("pythonGame/phone.txt", 'r', encoding='utf-8')
lines = file.readlines()

print(lines)


outfile = open('pythonGame/phone_modified.txt', 'w', encoding='utf-8')

for l in lines :
    outfile.write(l)
    
outfile.write('전우치 010-1000-2000')

file.close()
outfile.close()