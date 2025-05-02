file = open('pythonGame/read.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

words = {}
for l in lines :
    tmp = l.split(' ')
    for k in tmp :
        if (k == '\n') : continue
        k = k.lower()
        k = k.split(',')[0] if ',' in k else k.split('.')[0]
        words[k] = 1 if k not in words.keys() else words[k] + 1

sorted = list(words.keys())
sorted.sort()
file = open('pythonGame/out.txt', 'w', encoding='utf-8')

for k in sorted :
    file.write(f"{k} {words[k]}\n")
    
file.close()