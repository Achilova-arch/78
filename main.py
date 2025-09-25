son1=input("Birinchi son kiriting")
son2=input("Ikinchi son kiriting")
son3=input("Uchinchi son kiriting")
son4=input("Tortinhi son kiriting")
son5=input("Beshinchi son kiriting")
print(son1+son2+son3+son4+son5)




counter=0
for son in range(1,21):
    if son % 2 ==0:
        print(son)
        counter+=son
print(counter)

raqam = int(input("Son kiriting, men uni factorial hisoblb beraman:"))
fact=1
for son in range(1,raqam+1):
    fact *= son
print(fact)


ism=input("Ism kiriting, men bu ismn unli harflarini olb tashliman:")
text=ism
for harf in text:
    if harf not in "aioue":
        print(harf)