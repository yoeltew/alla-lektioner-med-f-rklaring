# Hej! Det här är din första Python-lektion.
# Rader som börjar med # är kommentarer - datorn läser inte dessa,
# de är bara för oss människor att förstå koden bättre!

# ============= LEKTION 1: FÖRSTA PROGRAMMET =============

# Så här skriver man ut text på skärmen:
print("Hej! Detta är mitt första program!")

# Vi kan också spara information i variabler
# Tänk på variabler som lådor där du kan spara saker
namn = "Anna"       # En låda som innehåller text
ålder = 15         # En låda som innehåller ett nummer
gillar_glass = True  # En låda som innehåller ja/nej (True/False)

# Nu kan vi använda våra variabler
print("Hej, jag heter " + namn)
print("Jag är", ålder, "år gammal")

# Vi kan göra matematik med variabler
pocket_money = 100
glass_kostnad = 20
pengar_kvar = pocket_money - glass_kostnad
print("Om jag köper en glass för", glass_kostnad, "kr kommer jag ha", pengar_kvar, "kr kvar")

# ============= FRÅGA ANVÄNDAREN OM SAKER =============
# input() låter användaren skriva något
ditt_namn = input("Vad heter du? ")
print("Trevligt att träffas,", ditt_namn, "!")

# När vi får nummer från input måste vi konvertera dem från text till nummer
din_ålder = input("Hur gammal är du? ")
din_ålder_som_nummer = int(din_ålder)  # Gör om text till heltal
år_till_18 = 18 - din_ålder_som_nummer
print("Om", år_till_18, "år kommer du vara 18!")

# ============= PROVA SJÄLV! =============
# 1. Skapa en variabel med ditt favoritdjur
# 2. Skapa en variabel med din favoritfärg
# 3. Skriv ut en mening som använder båda variablerna

# Till exempel:
favoritdjur = "katt"
favoritfärg = "blå"
print("Jag vill ha en", favoritfärg, favoritdjur)

# ============= LITE ROLIG MATEMATIK =============
# Vi kan göra olika sorters matematik
tal1 = 10
tal2 = 3

addition = tal1 + tal2        # Plus
subtraktion = tal1 - tal2     # Minus
multiplikation = tal1 * tal2  # Gånger
division = tal1 / tal2        # Delat med

print("Om vi har talet", tal1, "och talet", tal2)
print("Plus:", addition)
print("Minus:", subtraktion)
print("Gånger:", multiplikation)
print("Delat:", division)

# ============= TIPS OCH TRICKS =============
# 1. Kom ihåg att spara dina ändringar!
# 2. Om något går fel, kolla efter felstavningar
# 3. Var noga med citattecken (" ") runt text
# 4. Prova dig fram - det är så man lär sig!

# ============= UTMANING! =============
# Kan du göra ett program som:
# 1. Frågar efter användarens namn
# 2. Frågar efter användarens ålder
# 3. Räknar ut vilket år användaren fyller 100 år
# 4. Skriver ut resultatet i en rolig mening

# Tips: För att få nuvarande år kan du skriva:
from datetime import datetime
nuvarande_år = datetime.now().year