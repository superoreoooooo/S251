distanceMap = {"수성" : 91700000, "금성" : 41400000, "화성" : 78400000, "목성" : 628700000, "토성" : 1277400000, "천왕성" : 2750400000, "해왕성" : 4347400000}

planet = input("planet : ")
speed = int(input("speed : "))

hr = distanceMap[planet] / speed

print(f"약 {hr} 시간")
print(f"약 {int(int(hr) / (365 * 24))} 년")#ㅇㄴㄴㅁㄹㅁㄴ어ㅏㅁㄴㅇ리ㅏㅁㄴ어ㅏㅣ미ㅏㅓㄴ