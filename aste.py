def lasit_datni():
    # pajautāsim ievadīt datnes nosaukumu
    datnes_nosaukums=input("Ievadīt datnes nosaukumu: ")
    try:
    # kā ielādēt datnes saturu?
        with open(datnes_nosaukums, 'r') as ff:
            saturs=ff.read()
            # print(saturs) pārliecinājos par to, ka datnē ir skaitļi
            print(f"Simbolu skaits datnē ir {len(saturs)}")
            #izvadi pirmos desmit simbolus
            print(f"Pirmie 10 simboli ir:{saturs[:10]}")
            #izvadi pirmo un pēdējo simbolu
            print(f"Izvadi pirmo un pēdējo simbolu: {saturs[0]} un {saturs[-1]}")
    except FileNotFoundError:
        print("Datne nav atrasta!")
    except ValueError:
        print("Datu kļūda")


if __name__=="__main__":
    lasit_datni()