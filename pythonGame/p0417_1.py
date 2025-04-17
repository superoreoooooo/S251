temp_list = [0, 10, 20, 30]
vapor_list = [4.8, 9.4, 17.3, 30.4]

temp = int(input("temp : "))
vapor = float(input("vapor : "))

if (temp in temp_list) :
    humidity = vapor / vapor_list[temp_list.index(temp)] * 100
    print(f"humidity : {humidity:.1f}")
else :
    print("error!")