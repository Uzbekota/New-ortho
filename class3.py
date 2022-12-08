condyle=input("Bo'g'im boshchasining holatini kiriting:\n (Eslatma, shulardan birini tanlang\n 'Anterior, Normal, Distal' ")
S_Na=int(input("Sella-Nazion qiymatini millimetrlarda kiriting: "))
Go_Gn=int(input("Gonion-Gnation qiymatini millimetrlarda kiriting: "))
SNA=int(input("SNA qiymatini kiriting: "))
vertebra=int(input("Bo'yin umurtqalarining shakllanish bosqichini kiriting (1-6 gacha): "))
overjet=int(input("Over Jet qiymatini kirirting: "))
simptom=input("Bo'g'imda simptom bormi? (Ha yoki Yo'q): ")

def yopish():
    print("Kirgizilgan malumotlarni qayta tekshiring !")

if condyle in ['Normal']:
    if S_Na==Go_Gn and SNA<82:

        if vertebra in [1,2,3,4]:
            print("Modifikatsiya")

        elif vertebra in [5,6]:
            if overjet >=-4:
                print("Komufulyaj")

            elif overjet<-4:
                print("Xirurgiya")

            else:
                yopish()    
        else:
            yopish()

    elif S_Na<Go_Gn and SNA==82:
        if vertebra in [1,2,3,4]:
            print("Modifikatsiya")

        elif vertebra in [5,6]:
            if overjet >=-4:
                print("Komufulyaj")

            elif overjet<-4:
                print("Xirurgiya")

            else:
                yopish()   
        else:
            yopish()
    else:
        yopish()

elif condyle in ['Distal']:
    if S_Na==Go_Gn and SNA<82:
        if simptom in["Yo'q"]:
            if vertebra in [1,2,3,4]:
                print("Modifikatsiya")

            elif vertebra in [5,6]:
                if overjet >=-4:
                    print("Komufulyaj")
                else:
                    yopish()
            else:
                yopish()

        elif simptom in ["Ha"]:
            if vertebra in [1,2,3,4]:
                print("18 yoshgacha kutiladi,CR, keyin xirurgiya")

            elif vertebra in [5,6]:
                print("CR, keyin xirurgiya")
            else:
                yopish()
        else:
            yopish()

    elif S_Na<Go_Gn and SNA==82:
        if simptom in["Yo'q"]:
            if vertebra in [1,2,3,4]:
                print("Modifikatsiya")

            elif vertebra in [5,6]:
                if overjet >=-4:
                    print("Komufulyaj")
                else:
                    yopish()
            else:
                yopish()

        elif simptom in ["Ha"]:
            if vertebra in [1,2,3,4]:
                print("18 yoshgacha kutiladi,CR, keyin xirurgiya")

            elif vertebra in [5,6]:
                print("CR, keyin xirurgiya")
            else:
                yopish()
        else:
            yopish()

    else:
        yopish()

else:
    yopish()       
