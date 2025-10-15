# Lektion 2 - Listor och Loopar
# Här lär vi oss hur man jobbar med många saker på en gång!

# ============= LISTOR =============
# En lista är som en låda med flera fack
# Varje sak i listan har ett nummer som börjar på 0

# Skapa en lista med favoritfrukter
frukter = ["äpple", "banan", "apelsin", "päron"]
print("Mina favoritfrukter är:", frukter)

# Hämta en specifik frukt (kom ihåg, vi börjar räkna från 0!)
första_frukten = frukter[0]  # Detta är "äpple"
andra_frukten = frukter[1]   # Detta är "banan"
print("Min första frukt är:", första_frukten)
print("Min andra frukt är:", andra_frukten)

# ============= FOR-LOOPAR =============
# En for-loop är som att säga "gör detta för varje sak i listan"

# Skriv ut varje frukt
print("\nHär är alla mina frukter:")  # \n gör en ny rad
for frukt in frukter:
    print("- " + frukt)

# Räkna 1 till 5
print("\nLåt oss räkna till 5:")
for nummer in range(1, 6):  # range(1, 6) ger numren 1, 2, 3, 4, 5
    print("Nummer:", nummer)

# ============= WHILE-LOOPAR =============
# En while-loop fortsätter så länge något är sant

# Räkna ner från 5
print("\nNedräkning:")
nedräkning = 5
while nedräkning > 0:
    print(nedräkning)
    nedräkning = nedräkning - 1
print("Start!")

# ============= ROLIGA EXEMPEL =============

# 1. Gör en lista med kompisar och hälsa på alla
kompisar = ["Kim", "Alex", "Sam", "Robin"]
for kompis in kompisar:
    print("Hej", kompis, "! Ha en bra dag!")

# 2. Gör en enkel multiplikationstabell
print("\nTvåans tabell:")
for nummer in range(1, 11):
    resultat = 2 * nummer
    print("2 x", nummer, "=", resultat)

# 3. Göra en "gissa talet"-lek
import random
hemligt_tal = random.randint(1, 10)
gissning = 0
försök = 0

print("\nGissa talet mellan 1 och 10!")
while gissning != hemligt_tal and försök < 3:
    gissning = int(input("Din gissning: "))
    försök = försök + 1
    
    if gissning == hemligt_tal:
        print("Rätt! Du klarade det!")
    elif försök == 3:
        print("Tyvärr! Det hemliga talet var", hemligt_tal)
    else:
        if gissning < hemligt_tal:
            print("För lågt! Försök igen!")
        else:
            print("För högt! Försök igen!")

# ============= PROVA SJÄLV! =============
# 1. Gör en lista med dina favoritfilmer
# 2. Använd en for-loop för att skriva ut dem
# 3. Lägg till en numrering (1. Film, 2. Film, osv)

# 4. Extra utmaning: Gör en inköpslista där användaren
#    får lägga till saker tills de skriver "klar"