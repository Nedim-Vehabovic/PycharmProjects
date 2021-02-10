print("Pozdravljeni. Veseli nas, da uporabljate naš pretvornik.")

print("Vnesite število km, ki jih želite pretvoriti v milje:  ")

spremenljivka = int(input())
print("Vaša vrednost je " + str(spremenljivka * 0.6214) + " mi")

pozitiven = str("da")
negativen = str("ne")
while True:
    odgovor = str(input("Ali želite še eno pretvorbo (da/ne)?"))

    if odgovor == pozitiven:
        print("Vnesite število km, ki jih želite pretvoriti v milje:  ")
        spremenljivka = int(input())
        print("Vaša vrednost je " + str(spremenljivka * 0.6214) + " mi")

    elif odgovor == negativen:
        print("Goodbye")
        break

    else:
        print("Neznan odgovor. Goodbye")
        break









