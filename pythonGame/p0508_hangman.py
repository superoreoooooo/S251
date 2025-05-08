import random

words = [
    "apple", "house", "table", "water", "music",
    "river", "chair", "mouse", "bread", "plant",
    "guitar", "yellow", "coffee", "castle", "island",
    "rocket", "shadow", "puzzle", "window", "garden",
    "xylophone", "astronomy", "jazz", "mystery", "rhythm",
    "knapsack", "oxygen", "zodiac", "whisper", "voyage"
]

word = random.choice(words)
tryCnt = 10
t = ['_' for _ in range(0, len(word), 1)]

print(word)

while True :
    if (tryCnt <= 0) :
        print("failed!")
        break
        
    ip = input("단어를 추측하세요: ")
    if (len(ip) != 1) :
        print("wrong input!")
        continue
    if (ip in word) :
        for k in range(0, len(word), 1) : 
            if (ip == word[k]) :
                t[k] = ip
    print(t)
    
    if ('_' not in t) :
        print("success!")
        break
    
    tryCnt -= 1