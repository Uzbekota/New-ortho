condyle=input("Bo'g'im boshchasining holatini kiriting:\n (Eslatma, shulardan birini tanlang\n 'Anterior, Normal, Distal' ")
S_Na=int(input("Sella-Nazion qiymatini millimetrlarda kiriting: "))
Go_Gn=int(input("Gonion-Gnation qiymatini millimetrlarda kiriting: "))
vertebra=int(input("Bo'yin umurtqalarining shakllanish bosqichini kiriting (1-6 gacha): "))
overjet=int(input("Over Jet qiymatini kirirting: "))

if condyle in ['Normal', S_Na>Go_Gn,]:
    if vertebra in [1,2,3,4]:
        print("Modifikatsiya")

    elif vertebra in [5,6]:
        if 0<= overjet < 10:
            print("Komufulyaj")

        elif overjet >= 10:
            print("Xirurgiya")
        else:
            print("Kirgizilgan malumotlarni qayta tekshiring !")
    else:
        print("Kirgizilgan malumotlarni qayta tekshiring !")    

elif condyle in ['Distal']:
    if S_Na == Go_Gn:
        print("Anterizatsia")

    elif S_Na>Go_Gn:
        if vertebra in [1,2,3,4]:
            print("Ko'p bosqichli Modifikatsiya")

        elif vertebra in [ 5,6]:
            if 0<= overjet <10:
                print("Komufulyaj")

            elif overjet>=10:
                print("Xirurgiya")
            else:
                print("Kirgizilgan malumotlarni qayta tekshiring !")   
        else:
            print("Kirgizilgan malumotlarni qayta tekshiring !")        
    else:
        print("Kirgizilgan malumotlarni qayta tekshiring !")
else:
    print("Kirgizilgan malumotlarni qayta tekshiring !")
