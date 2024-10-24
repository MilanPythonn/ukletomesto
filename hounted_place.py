import time


print("DOBRODOSLI U IGRU:\nUKLETO MESTO\n-------------------------------------\n"
      "CILJ IGRE JE DA NAĐEŠ IZLAZ DO GRADA.\n\n"
      "NALAZIŠ SE NA CESTI UKLETOG MESTA U SVOM VOZILU.\n"
      "SVE ŠTO IMAŠ KOD SEBE JE ︻┳デ═— .")
time.sleep(1)
izbor1 = input("DA POKRENEŠ VOZILO I KRENEŠ NAPRED UPIŠI 'napred': ").lower()

if izbor1 == "napred":
    time.sleep(1)
    print("""    ) )        /\
   =====      /  \
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;""")
    print("\nI TAKO SE VOZIŠ CESTOM DOK NE NAIĐEŠ NA KUĆU KOJA SE NALAZI PORED CESTE I IZGLEDA VEOME ČUDNO.")
    time.sleep(1)
    izbor2 = input("DA LI ĆEŠ UĆI? UPIŠI 'ulazim' AKO ZELIŠ IĆI DALJE UPIŠI 'dalje': ").lower()
    if izbor2 == "ulazim":
        time.sleep(1)
        print("IZABRAO SI DA UĐEŠ, ALI POSTOJI PROBLEM! KUĆA JE ZAKLJUČANA!\n")
        time.sleep(1)
        izbor3 = input("DA LI ŽELIŠ OTKLJUČATI ILI SE VRATITI U VOZILO?\n"
                       "AKO ŽELIŠ OTKLJUČATI UPIŠI 'otvaram' AKO SE ŽELIŠ VRATITI 'nazad': ").lower()
        time.sleep(1)
        if izbor3 == "otvaram":
            time.sleep(1)
            zagonetka = input("\nDA OTKLJUČAŠ VRATA MORAŠ REŠITI ZAGONETKU:\n"
                              "ŠTA MOŽE DA LETI BEZ KRILA U PLAČE BEZ OČIJU?: ").lower()
            if zagonetka == "oblak":
                time.sleep(1)
                print("POGODILI STE ZAGONETKU I OTVORILI VRATA.\n")
                time.sleep(1)
                print("ULAZITE I VIDITE STEPENICE KOJE VODE NA SPRAT IZNAD.\n")
                time.sleep(1)
                izbor4 = input("DA LI ŽELITE IĆI NA SPRAT?\nAKO DA UPIŠITE 'da' ILI 'ne' ZA OBRNUTO: " ).lower()
                if izbor4 == "da":
                    time.sleep(1)
                    print("POLAKO KORAČATE UZ STEPENICE I UGLEDATE MNOGO KRVI I ISKASAPLJENA TJELA!\n")
                    time.sleep(1)
                    print("POČINJETE DA SE PLAŠITE. VRATA SPOREDNE SOBE SE OTVARAJU I UGLEDATE OSOBU\n"
                          "KOJA NOSI MAČETU I UBIJA VAS!\nGAME OVER!")
                    time.sleep(1)
                    print(""" (╯︵╰,)""")
                elif izbor4 == "ne":
                    time.sleep(1)
                    print("U PROSTORIJI ISPRED VAS SE NALAZI NEŠTO VRIJEDNO, POKUŠAJTE NAĆI.\n")
                    time.sleep(1)
                    print("DA BI PRONAŠAO NEŠTO VREDNO MORAŠ BITI TIH I KRENUTI U PROSTORIJU.\n")
                    time.sleep(1)
                    print("OKO SEBE VIDIŠ STARE STOLOVE,STOLICE ALI TI ZA OKO PADNE KREDENAC KOJI IMA SAMO JEDNU LADICU\n")
                    time.sleep(1)
                    otvori = input("SVE ŠTO MOŽEŠ JE DA OTVORIŠ TU LADICU KOMANDOM 'otvori': ").lower()
                    if otvori == "otvori":
                        time.sleep(1)
                        print("USPEŠNO OTVARAŠ TE NALAZIŠ ZLATNI KLJUČ KOJI ĆE TI BITI POTREBAN!\n")
                        time.sleep(1)
                        print("KLJUČ STAVLJAŠ U DŽEP I VRAĆAŠ SE U VOZILO.")
                        time.sleep(1)
                        print("\nI TAKO VOZIŠ DOK U TRENUTKU IZLETI MASKIRANO LICE SA LUKOM I STRELOM.\n")
                        print("""»»---------------------►""")
                        izbor5 = input("\nŠTA ĆEŠ URADITI? DA GA UBIJEŠ PUŠKOM UPIŠI 'puska', DA GA PREGAZIŠ UPIŠI 'gazim': ").lower()
                        if izbor5 == "puska":
                            time.sleep(1)
                            print("\nUZIMAM PUŠKU I UBIJAM SPODOBU!\n")
                            time.sleep(1)
                            print("IZLAZIM I PRILAZIM OSOBI.PRETRESAM GA,\n"
                                  "PRONALAZIM MAPU SA BLAGOM NA KOJOJ PIŠE 'kovčeg se otvara zlatnim ključom'\n")
                            time.sleep(1)
                            izbor6 = input("DA BI KRENUO ZA BLAGON UPIŠI 'da': ").lower()
                            if izbor6 == "da":
                                time.sleep(1)
                                print("KREČEŠ U ŠUMU U POTRAZI ZA BLAGOM.\n")
                                time.sleep(1)
                                print("TAKOĐER POSTOJI OSOBA KOJA TE VREBA SVAKOG TRENUTKA!\n")
                                time.sleep(1)
                                print("UZIMAŠ PUŠKU U RUKE I NASTAVLJAŠ.ISPRED TEBE IZLAZI JOŠ JEDNA MASKIRANA SPODOBA")
                                time.sleep(1)
                                print("KOJA TI ZABIJA STRELU U SRCE\n")
                                time.sleep(1)
                                print("IGRA JE ZA TEBE GOTOVA. VIŠE SREĆE DRUGI PUT!")
                            else:
                                time.sleep(1)
                                print("POGREŠAN IZBOR, PAZI KAKO PIŠEŠ. GAME OVER!")
                                print(""" (╯︵╰,)""")

                        elif izbor5 == "gazim":
                            time.sleep(1)
                            print("DODAJEŠ GAS I GAZIŠ SPODOBU\n")
                            time.sleep(1)
                            print("NASTAVLJAŠ PUT DALJE!\n")
                            time.sleep(1)
                            izbor6 = input("NAILAZIŠ DA RASKRSNICU KOJA VODI DESNO I LIJEVO\n"
                                           "ŠTA BIRAS? 'desno' ili 'lijevo': ").lower()
                            if izbor6 == "desno":
                                time.sleep(1)
                                print("IZABRAO SI I KRENUO DESNO,\nVRAĆAŠ SE NA ISTO MJESTO SA POČETKA!")
                                time.sleep(1)
                                print("GAME OVER!")
                                print(""" (╯︵╰,)""")
                            elif izbor6 == "lijevo":
                                time.sleep(1)
                                print("IZABRAO SI I KRENUO LIJEVO.\n")
                                time.sleep(1)
                                print("USPEŠNO SI DOŠAO U GRAD I SPASAO SE!")
                                time.sleep(1)
                                print("ČESTITAM TI NA POBJEDI\n,")
                                time.sleep(1)
                                print("NADAM SE DA TI SE IGRICA SVIDJELA.\nKREIRAO JE MILAN GACO\n"
                                      "POČETNIK PROGRAMSKOG JEZIKA PYTHON!")
                            else:
                                time.sleep(1)
                                print("POGREŠAM IZBOR! GAME OVER!")
                                print(""" (╯︵╰,)""")
                    else:
                        time.sleep(1)
                        print("POGREŠNA KOMANDA! GAME OVER!")
                        print(""" (╯︵╰,)""")
            else:
                time.sleep(1)
                print("POGREŠAN ODGOVOR! GAME OVER!")
                print(""" (╯︵╰,)""")
        elif izbor3 == "nazad":
            time.sleep(1)
            print("ZANEMARUJEŠ KUĆU I NASTAVLJAŠ DALJE.\n")
            time.sleep(1)
            print("""»»---------------------►""")
            print("\nI TAKO VOZIŠ DOK U TRENUTKU IZLETI MASKIRANO LICE SA LUKOM I STRELOM.")
            time.sleep(1)
            izbor5 = input("ŠTA ĆEŠ URADITI? DA GA UBIJEŠ PUŠKOM UPIŠI 'puska', DA GA PREGAZIŠ UPIŠI 'gazim': ").lower()
            if izbor5 == "puska":
                time.sleep(1)
                print("\nUZIMAM PUŠKU I UBIJAM SPODOBU!\n")
                time.sleep(1)
                print("IZLAZIM I PRILAZIM OSOBI.PRETRESAM GA,\n"
                      "PRONALAZIM MAPU SA BLAGOM NA KOJOJ PIŠE 'kovčeg se otvara zlatnim ključom'\n")
                time.sleep(1)
                izbor6 = input("DA BI KRENUO ZA BLAGON UPIŠI 'da': ").lower()
                if izbor6 == "da":
                    time.sleep(1)
                    time.sleep(1)
                    print("KREČEŠ U ŠUMU U POTRAZI ZA BLAGOM.\n")
                    time.sleep(1)
                    print("TAKOĐER POSTOJI OSOBA KOJA TE VREBA SVAKOG TRENUTKA!\n")
                    time.sleep(1)
                    print("UZIMAŠ PUŠKU U RUKE I NASTAVLJAŠ.ISPRED TEBE IZLAZI JOŠ JEDNA MASKIRANA SPODOBA")
                    time.sleep(1)
                    print("KOJA TI ZABIJA STRELU U SRCE\n")
                    time.sleep(1)
                    print("IGRA JE ZA TEBE GOTOVA. VIŠE SREĆE DRUGI PUT!")
                else:
                    time.sleep(1)
                    print("POGREŠAN IZBOR, PAZI KAKO PIŠEŠ. GAME OVER!")
                    print(""" (╯︵╰,)""")

            elif izbor5 == "gazim":
                time.sleep(1)
                print("DODAJEŠ GAS I GAZIŠ SPODOBU I NASTAVLJAŠ PUT DALJE!\n")
                time.sleep(1)
                izbor6 = input("NAILAZIŠ DA RASKRSNICU KOJA VODI DESNO I LIJEVO\n"
                               "ŠTA BIRAS? 'desno' ili 'lijevo': ").lower()
                if izbor6 == "desno":
                    time.sleep(1)
                    print("IZABRAO SI I KRENUO DESNO,\nVRAĆAŠ SE NA ISTO MJESTO SA POČETKA!\nGAME OVER")
                    print(""" (╯︵╰,)""")
                elif izbor6 == "lijevo":
                    time.sleep(1)
                    print("IZABRAO SI I KRENUO LIJEVO.\n")
                    time.sleep(1)
                    print("USPEŠNO SI DOŠAO U GRAD I SPASAO SE!")
                    time.sleep(1)
                    print("ČESTITAM TI NA POBJEDI\n,")
                    time.sleep(1)
                    print("NADAM SE DA TI SE IGRICA SVIDJELA.\nKREIRAO JE MILAN GACO\n"
                          "POČETNIK PROGRAMSKOG JEZIKA PYTHON!")

    elif izbor2 == "dalje":
        time.sleep(1)
        print("\nZANEMARUJEŠ KUĆU I NASTAVLJAŠ DALJE.\n")
        time.sleep(1)
        print("""»»---------------------►""")
        print("\nI TAKO VOZIŠ DOK U TRENUTKU IZLETI MASKIRANO LICE SA LUKOM I STRELOM.")
        time.sleep(1)
        izbor5 = input("ŠTA ĆEŠ URADITI? DA GA UBIJEŠ PUŠKOM UPIŠI 'puska', DA GA PREGAZIŠ UPIŠI 'gazim': ").lower()
        if izbor5 == "puska":
            time.sleep(1)
            print("\nUZIMAM PUŠKU I UBIJAM SPODOBU!\n")
            time.sleep(1)
            print("IZLAZIM I PRILAZIM OSOBI.PRETRESAM GA,\n"
                  "PRONALAZIM MAPU SA BLAGOM NA KOJOJ PIŠE 'kovčeg se otvara zlatnim ključom'\n")
            time.sleep(1)
            izbor6 = input("DA BI KRENUO ZA BLAGON UPIŠI 'da': ").lower()
            if izbor6 == "da":
                time.sleep(1)
                print("KREČEŠ U ŠUMU U POTRAZI ZA BLAGOM.\n")
                time.sleep(1)
                print("TAKOĐER POSTOJI OSOBA KOJA TE VREBA SVAKOG TRENUTKA!\n")
                time.sleep(1)
                print("UZIMAŠ PUŠKU U RUKE I NASTAVLJAŠ.ISPRED TEBE IZLAZI JOŠ JEDNA MASKIRANA SPODOBA KOJA TI ZABIJA STRELU U SRCE\n")
                time.sleep(1)
                print("IGRA JE ZA TEBE GOTOVA. VIŠE SREĆE DRUGI PUT!")
                print(""" (╯︵╰,)""")
            else:
                time.sleep(1)
                print("POGREŠAN IZBOR, PAZI KAKO PIŠEŠ. GAME OVER!")
                print(""" (╯︵╰,)""")

        elif izbor5 == "gazim":
            time.sleep(1)
            print("DODAJEŠ GAS I GAZIŠ SPODOBU I NASTAVLJAŠ PUT DALJE!\n")
            time.sleep(1)
            izbor6 = input("NAILAZIŠ DA RASKRSNICU KOJA VODI DESNO I LIJEVO\n"
                           "ŠTA BIRAS? 'desno' ili 'lijevo': ").lower()
            if izbor6 == "desno":
                time.sleep(1)
                print("IZABRAO SI I KRENUO DESNO,\nVRAĆAŠ SE NA ISTO MJESTO SA POČETKA1")
                time.sleep(1)
                print("GAME OVER!")
                print(""" (╯︵╰,)""")
            elif izbor6 == "lijevo":
                time.sleep(1)
                print("IZABRAO SI I KRENUO LIJEVO.\n")
                time.sleep(1)
                print("USPEŠNO SI DOŠAO U GRAD I SPASAO SE!")
                time.sleep(1)
                print("ČESTITAM TI NA POBJEDI\n,")
                time.sleep(1)
                print("NADAM SE DA TI SE IGRICA SVIDJELA.\nKREIRAO JE MILAN GACO\n"
                      "POČETNIK PROGRAMSKOG JEZIKA PYTHON!")
            else:
                time.sleep(1)
                print("PRAVO NE MOZES! GAME OVER!")
                print(""" (╯︵╰,)""")
        else:
            time.sleep(1)
            print("POGREŠAM IZBOR! GAME OVER!")
            print(""" (╯︵╰,)""")
    else:
        time.sleep(1)
        print("NISI ODABRAO PONUĐENO. GAME OVER!")
        print(""" (╯︵╰,)""")
else:
    time.sleep(1)
    print("UPIŠI 'napred' JESI ĆORAV?")
    print(""" (╯︵╰,)""")