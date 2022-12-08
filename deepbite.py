condyle=input("Bo'g'im boshchasining holatini kiriting:\n (Eslatma, shulardan birini tanlang\n 'Anterior, Normal, Distal' ")
overbite=int(input("Over Bite qiymatini kiriting: "))
fma=int(input("FMA qiymatini kiriting: "))
typesmile=input("Smile turini kiriting: 'Quyidagilardan birini tanlang: Upper, Normal, Lower': ")
vertebra=int(input("Bo'yin umurtqalarining shakllanish bosqichini kiriting (1-6 gacha): "))

def yopish():
    print("Kirgizilgan malumotlarni qayta tekshiring !")


if condyle in ['Normal' 'normal','Norma','norma']:
    if -1>= overbite >= -3:
        print("Bemorda deep bite yo'q !")

    elif overbite < -3:
        if typesmile in ['Lower','lower']:
            if fma == 25:
                print("Yuqori kesuv tishlar intruziyasi.")
            else:
                yopish()

        elif typesmile in ['Lower', 'lower', 'Normal','normal','Norma','norma']:
            if fma<25:
                if vertebra in [1,2,3,4]:
                    print("Modifikatsiya, Molyar tishlar ekstruziyasi")

                elif vertebra in [5,6]:
                    print("Kamufulyaj: old tishlar intruziyasi va jag rotatsiyasi ")    

                else:
                    yopish()    

            else:
                yopish()
        else:
            yopish()            
    else:
        yopish()
elif condyle in ['Distal','distal']:
    if typesmile in ['Lower','lower']:
        print("Anterizatsiya + Old tishlar intruziyasi. ")

    elif typesmile in ['Normal','normal','Norma','norma']:
        print("Anterizatsiya + Yon tishlar ekstruziyasi")

    else:
        yopish()    

else:
    yopish()