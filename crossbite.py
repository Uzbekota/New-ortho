Mx=int(input("Yuqori jag'ning o'lchamini kiriting: "))
Mn=int(input("Pastki jag'ning o'lchamini kiriting: "))
chok= input('Chokning holatini kiriting: ')
yosh=int(input("yoshini kriting: "))
tishx=input("Yon guruh tishlar kesishgan holatdami ?,\n (Eslatma: agar bemorda, yashiringan cross bite bo'lsa ham\n 'Ha' deb yozing! ) : ") #dental cross bite ning bor yo'qligi haqida so'rayapdi

if (Mx-Mn < 5):
    if chok in ['A','a','B','b','C','c']:
        if yosh <=9:
            print("Marco Rosso")
        elif 9< yosh <=14:
            print("Hyrax")
        elif 16 <= yosh <=60:
            print("MSE")
        else :
            print("Bemorga ortodontik davolash kerakligiga shubxam bor !")

    elif chok in ['D','d','E','e']:
        print("SARPE")

    else:
        print("Chok haqida malumot noto'g'ri malumot kiritildi")    


else:
    if tishx in ["Ha", "ha", "HA","Xa", "XA", "xa"]:
        print("Dental expansion:\n>>> Misol uchun: Muligan yoyi")
    else:
        print("Bemorda skeletal va dental cross bite yo'q.")    
