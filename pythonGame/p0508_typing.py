import random
import time

words = [
    "apple", "house", "table", "water", "music",
    "river", "chair", "mouse", "bread", "plant",
    "guitar", "yellow", "coffee", "castle", "island",
    "rocket", "shadow", "puzzle", "window", "garden",
    "xylophone", "astronomy", "jazz", "mystery", "rhythm",
    "knapsack", "oxygen", "zodiac", "whisper", "voyage"
]

start = time.time()

def question(q, cnt) :
    print(f"*문제 {cnt + 1}")
    print(q)
    
    if (q == input()) :
        print("통과!")
        # print(f"T NOW : {(time.time() - start):.2f}초")
        return True
    else :
        print("오타!")
        question(q, cnt)

for i in range(0, 5, 1) :
    q = random.choice(words)
    words.remove(q)
    
    if (question(q, i) == True) :
        continue
                    
end = time.time()

print(f"타자 시간 : {(end - start):.2f}초")