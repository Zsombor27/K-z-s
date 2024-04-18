from random import randint

veletlen = {}
for n in range(1000):
    e = randint(0,100)
    if e in veletlen:
        veletlen[e] += 1
    else:
        veletlen[e]=1

leggy = max(veletlen.values())
maxlist= []

print("Agenerált eőfordulásai és véletlenszámok:",veletlen)

for k in veletlen:
    if veletlen[k] == leggy:
        maxlist.append(k)

    print("A generált véletlenszámok és előfordulásaik száma.")
    print(veletlen)
    print("Alegnagyobb előfordulási szám:",leggy)
    print("Ez(ek) a Szám(ok) fordult(ak) elő a leggyakrabban.")
    for k in veletlen:
        if veletlen[k] == leggy:
            maxlist.append(k)