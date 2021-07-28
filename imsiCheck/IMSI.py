# import PySimpleGUI as sg
# sg.Window(title="IMSI simple check", layout=[[]], margins=(300,150)).read()
from lista import operators
import os
# operators = {
#     "Polkomtel Sp. z o.o..": "01",
#     "T-MOBILE POLSKA S.A..": "02",
#     "Orange Polska S.A..": "03",
#     "AERO 2 Sp. z o.o.": "04",
#     "Orange Polska S.A.": "05",
#     "P4 Sp. z o.o.": "06",
#     "Netia S.A.": "07",
#     "Rezerwa Prezesa UKE.": "08",
#     "Lycamobile Sp. z o.o.": "09",
#     "T-MOBILE POLSKA S.A...": "10",
#     "Polkomtel Sp. z o.o.": "11",
#     "Cyfrowy POLSAT S.A.": "12",
#     "Move Telecom S.A.": "13",
#     "TELCO LEADERS LTD": "14",
#     "AERO 2 Sp. z o.o..": "15",
#     "AERO 2 Sp. z o.o...": "16",
#     "AERO 2 Sp. z o.o....": "17",
#     "AMD Telecom SA (2)": "18",
#     "SIA NetBalt": "19",
#     "TISMI B.V.": "20",
#     "MSWiA": "2101",
#     "Miejskie Przedsiębiorstwo Komunikacyjne Sp. z o.o. (Wrocław)": "2102",
#     "Przedsiębiorstwo Państwowe PORTY LOTNICZE": "2103",
#     "Gdynia Container Terminal S.A.": "2104",
#     "DCT Gdańsk S.A.": "2105",
#     "Autostrada Eksploatacja S.A.": "2106",
#     "Miejskie Przedsiębiorstwo Komunikacyjne S. A. (Kraków)": "2107",
#     "ENERGA - OPERATOR S.A.": "2108",
#     "Polski Koncern Naftowy ORLEN S.A..": "2109",
#     "BCT - Bałtycki Terminal Kontenerowy Sp. z o.o.": "2110",
#     "PGE Górnictwo i Energetyka Konwencjonalna S.A.": "2111",
#     "Port Lotniczy Rzeszów-Jasionka Sp. z o.o.": "2112",
#     "Port Lotniczy Gdańsk Sp. z o.o.": "2113",
#     "Mazowiecki Port Lotniczy Warszawa-Modlin Sp. z o.o.": "2114",
#     "Polski Koncern Naftowy ORLEN S.A.": "2115",
#     "Port Lotniczy Gdynia-Kosakowo Sp. z o.o.": "2116",
#     "Metro Warszawskie Sp. z o.o.": "2117",
#     "Polskie LNG S.A.": "2118",
#     "ORLEN POŁUDNIE S.A.": "2119",
#     "Polskie Towarzystwo Przesyłu i Rozdziału Energii Elektrycznej": "2120",
#     "Zarząd Morskiego Portu Gdynia S.A.": "2121",
#     "Twilio Ireland Limited": "22",
#     "PGE Systemy S.A.": "23",
#     "IT Partners Telco Sp. z o.o.": "24",
#     "Rezerwa Prezesa UKE2": "25",
#     "Rezerwa Prezesa UKE3": "26",
#     "SIA Ntel Solutions": "27",
#     "Rezerwa Prezesa UKE4": "28",
#     "Rezerwa Prezesa UKE5": "29",
#     "Rezerwa Prezesa UKE6": "30",
#     "Rezerwa Prezesa UKE7": "31",
#     "COMPATEL LIMITED": "32",
#     "Truphone Poland Sp. z o.o.": "33",
#     "T-MOBILE POLSKA S.A.": "34",
#     "PKP Polskie Linie Kolejowe S.A.": "35",
#     "Rezerwa Prezesa UKE8": "36",
#     "Rezerwa Prezesa UKE9": "37",
#     "Rezerwa Prezesa UKE10": "38",
#     'VOXBONE SA': "39",
#     "Rezerwa Prezesa UKE11": "40",
#     "EZ PHONE MOBILE Sp. z o.o.": "41",
#     "MobiWeb Telecom Limited": "42",
#     "Smart Idea International Sp. z o.o.": "43",
#     "Rezerwa Prezesa UKE12": "44",
#     "Virgin Mobile Polska Sp. z o.o.": "45",
#     "Rezerwa Prezesa UKE13": "46",
#     "SMSHIGHWAY LIMITED": "47",
#     "AGILE TELECOM S.P.A.": "48",
#     "Messagebird B.V.": "49",
#     "Polska Spółka Gazownictwa Sp. z o.o.": "90",
#     "Politechnika Łódzka Uczelniane Centrum Informatyczne": "97",
#     "P4 Sp. z o.o..": "98",
# }

print("""
 ▄▄▄▄▄▄▄▄▄▄▄       ▄▄       ▄▄       ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀      ▐░▌░▌   ▐░▐░▌     ▐░█▀▀▀▀▀▀▀▀▀       ▀▀▀▀█░█▀▀▀▀ 
     ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌                    ▐░▌     
     ▐░▌          ▐░▌ ▐░▐░▌ ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄           ▐░▌     
     ▐░▌          ▐░▌  ▐░▌  ▐░▌     ▐░░░░░░░░░░░▌          ▐░▌     
     ▐░▌          ▐░▌   ▀   ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌          ▐░▌     
     ▐░▌          ▐░▌       ▐░▌               ▐░▌          ▐░▌     
 ▄▄▄▄█░█▄▄▄▄      ▐░▌       ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌      ▄▄▄▄█░█▄▄▄▄ 
▐░░░░░░░░░░░▌     ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀ 
   ______                ____           ______             
 .~      ~. |         | |             .~      ~. |    ..'' 
|           |_________| |______      |           |..''     
|           |         | |            |           |``..     
 `.______.' |         | |___________  `.______.' |    ``.. 
 """)
print("V 0.3\n (C) by yankess\n")

# imsi = input("Wprowadź numer IMSI - \n\n")
# mcc = imsi[0:3]
# mnc_two = imsi[3:5]
# mnc_three = imsi[3:6]
# mnc_four = imsi[3:7]

# print(mcc)
# print(mnc_two)
# print(mnc_three)
# print(mnc_four)
test = True

def sprawdzenie():
    imsi = input("Wprowadź numer IMSI (wystarczy pierwsze 7 cyfr) - \n\n   ")
    mcc = imsi[0:3]
    mnc_two = imsi[3:5]
    mnc_three = imsi[3:6]
    mnc_four = imsi[3:7]
    for k, v in operators.items():
        if v == mnc_two:
            print(f"\n-> Operator: {k}")
        elif v == mnc_three:
            print(f"\n-> Operator: {k}")
        elif v == mnc_four:
            print(f"\n-> Operator: {k}")
        # elif not v == mnc_two and mnc_three and mnc_four:
        #     print("\nBrak odpowiedzi, sprawdź poprawność numeru IMSI.")
        #     break
    question = input("\n---- Sprawdzić jeszcze jakiś numer? T/N ----\n").lower()
    global test
    if question == "t":
        while test:
            sprawdzenie()
    else:
        test = False
        input("\n\nNaciśnij ENTER aby zamknąć...")
        exit()

def plik():
    f = open("imsi.txt", "r")
    read_list = f.readlines()
    check_list = []
    for num in read_list:
        imsi = num
        mcc = imsi[0:3]
        mnc_two = imsi[3:5]
        mnc_three = imsi[3:6]
        mnc_four = imsi[3:7]
        for k, v in operators.items():
            if v == mnc_two:
                print(f"\n{imsi} -> Operator: {k}\n")
                check_list.append(imsi + f" -> {k}")
            elif v == mnc_three:
                print(f"\n{imsi} -> Operator: {k}\n")
                check_list.append(imsi + f" -> {k}")
            elif v == mnc_four:
                print(f"\n{imsi} -> Operator: {k}\n")
                check_list.append(imsi + f" -> {k}")
    with open('imsi_sprawdzone.txt', 'w') as f:
        for item in check_list:
            f.write("%s\n\n" % item)
    print("---- Zapisano plik imsi_sprawdzone.txt ----\n")
    glob_quest()

def glob_quest():
    quest =input("Jeden numer, wybrać plik czy koniec? Wpisz - jeden/plik/koniec ").lower()
    if quest == "jeden":
        sprawdzenie()
    elif quest == "plik":
        plik()
    elif quest == "koniec":
        input("\n\nNaciśnij ENTER aby zamknąć...")
        exit()

glob_quest()