'''
Visszaszámlálás.

Egy rakéta indítása előtt több órával visszaszámlálást kezdenek és óránként egyet számolnak vissza a rakéta indításáig. 
A felhasználó határozza meg, hogy hány órás a visszaszámlálás. 
A visszaszámlálást minden órában egy órára felfüggeszthetik, ha valamilyen váratlan esemény – műszaki hiba, időjárási probléma – merül fel. 
Amikor a visszaszámlálás eléri a 0-t, a rakétát fellövik.

Írjon programot, amely a visszaszámlálás számait jeleníti meg a képernyőn! 
Természetesen nem kell a visszaszámlálás lépései között eltelni időnek – minden üzenet megjelenését azonnal követheti a következő. 
A visszaszámlálás minden lépésénél kérdezze meg a felhasználót, hogy az adott órában szükség volt-e a visszaszámlálás fölfüggesztésére! 
A visszaszámlálás megjelenítését követően a program írja ki, hogy a visszaszámlálás kezdetétől hány óra telt el – a visszaszámlálás eredetileg tervezett hosszát a felfüggesztésekkel megnövelve!
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Hány órás visszaszámlálást tervezünk? 5
Visszaszámlálás: 5
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 5
-----
Hány órás visszaszámlálást tervezünk? 4
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 7
'''

szam=int(input("Hány órás visszaszámlálást tervezünk? "))
print("Visszaszámlálás:", szam)
szam2=szam-1
szam3=0
while szam2 > 0: 
  valasz=input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
  if valasz == "i" :
    print("Visszaszámlálás:", szam2)
    szam3 +=1
  elif valasz == "n":
    print("Visszaszámlálás:", szam2)
  szam2 -= 1
print("A rakéta a visszaszámlálást követően ennyi órával indult: ", szam + szam3 )

