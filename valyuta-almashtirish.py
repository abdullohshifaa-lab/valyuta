import os 
os.system("cls")

import requests as rq

link = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

data = rq.get(link).json()
print("Valyutalar")
n = 1
for  i in range(len(data)):
    n+=1
    print(i,data[i]["CcyNm_UZ"])
s = int(input(">>> "))
if s < 0 or s > 74:
    print("Valyuta tanlanmadi")
else:
    valyuta = data[s]
    print(f"1 {data[s]["CcyNm_UZ"]} -> SO'M\n2 SO'M -> {data[s]["CcyNm_UZ"]}")
    l = int(input(">>> "))
    if l == 1:
        print(f"{data[s]["CcyNm_UZ"]}dan SOMga otqaziladi")
        u = int(input(f"{data[s]["CcyNm_UZ"]} >>> "))
        q = float(data[s]["Rate"]) * u
        print(q)
    elif l == 2:
        print(f"SOMdan {data[s]["CcyNm_UZ"]}ga otqaziladi")
        u = int(input(f"SOM >>> "))
        r = float(data[s]["Rate"])
        q = u / r
        print(f"{q:.2f}")