import random

a = random.sample([k for k in range(0, 10, 1)], 10)
print(a)

def sort(lst, dir) :
    l = lst.copy()
    for i in range(0, len(l), 1) :
        for j in range(i, len(l), 1) :
            if (dir == 0) :
                if (l[i] > l[j]) :
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
            elif (dir == 1) :
                if (l[i] < l[j]) :
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
    return l


"""
v = sort(a, 0)
vv = sort(a, 1)

print(v, vv)

"""

b = "Hello World!"

print(b[-5:0:-1])