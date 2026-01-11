#Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
""" Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

klaaside_arv = input("Kui palju vett sa joonud oled? Sisesta ära joodud klaaside arv (<4/<8/≥8)")
if klaaside_arv == "<4":
    print(f"Joo rohkem vett, keha vajab seda!")
elif klaaside_arv == "<8":
    print(f"Tubli, jätka samas vaimus!")
elif klaaside_arv == "≥8":
    print(f"Suurepärane, oled oma päevase eesmärgi täitnud!")
    
