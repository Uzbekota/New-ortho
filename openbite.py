condyle=input("Bo'g'im boshchasining holatini kiriting:\n (Eslatma, shulardan birini tanlang\n 'Anterior, Normal, Distal' ")
fma=int(input("FMA qiymatini kiriting: "))
overbite=int(input("Over Bite qiymatini kiriting: "))
typesmile=input("Smile turini kiriting: 'Quyidagilardan birini tanlang: Upper, Normal, Lower': ")
vertebra=int(input("Bo'yin umurtqalarining shakllanish bosqichini kiriting (1-6 gacha): "))

def umurtqa_bosqichi():
    if vertebra in [1,2,3,4]:
        print(" 18 yoshgacha kutiladi, keyin xirurgiya")
    elif vertebra in [5,6]:
        print("Xirurgiya")    

def yopish():
    print("Kirgizilgan malumotlarni qayta tekshiring !")


if condyle in ['Normal' 'normal','Norma','norma']:
    if fma == 25 and 1< overbite <6:
        print("Old tishlar ekstruziyasi.")

    elif fma>25 :
        if 1 < overbite < 6 :
            if vertebra in [1,2,3,4]:
                print(" Modifikatsiya:jag rotatsiyasi")
            elif vertebra in [5,6]:
                print("Komufulyaj: yon tishlar intruziyasi ")     
            else:
                yopish()    

        elif overbite>=6:
            umurtqa_bosqichi()
        else:
            yopish()    
    else:
        yopish()

elif condyle in ['Upper' 'upper','Up','up']:
    if 1 <= overbite <6:
        if typesmile in ['Upper' 'upper','Up','up']:
            print("Dekompressiya: jag rotatsiyasi, old tishlar ekstruziyasi ")
        elif typesmile in ['Normal' 'normal','Norma','norma']:
            print ("Dekompressiya: jag rotatsiyasi")  
        else:
            yopish()   

    elif overbite >= 6 :
        umurtqa_bosqichi()
    else:
        yopish()
else:
    yopish()        