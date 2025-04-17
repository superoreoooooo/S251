rsp = {"가위" : 0, "바위" : 1, "보" : 2}

import random

pc = random.choice(list(rsp.keys()))
print(pc)
pick = input("pick : ")

if (pick in list(rsp.keys())) :
    if (rsp[pick] == rsp[pc]) :
        print("draw!")
    elif (rsp[pick] - rsp[pc] == 1 or rsp[pick] - rsp[pc] == -2) :
        print("win!")
    else :
        print("lose!")