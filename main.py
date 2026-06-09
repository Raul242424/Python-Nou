def print_hi(name):
    print(f'Hi, {name}')
word = 'ana'
if __name__ == '__main__':
    print_hi('PyCharm')

p = bool(word.find(word[::-1])+1)
print(p)


# def verifica_nota():
#     while True:
#         try:
#             nota = float(input("Introduceti nota la examen (0-10): "))
#
#             if 0 <= nota <= 10:
#                 if nota >= 9:
#                     print("Excelent")
#                 elif nota >= 7:
#                     print("Bine")
#                 elif nota >= 5:
#                     print("Suficient")
#                 else:
#                     print("Reexaminare")
#                 break
#             else:
#                 print("Eroare: Introdu o valoare intre 0 si 10.")
#
#         except ValueError:
#             print("Eroare: Introdu un numar valid.")
#
#
# if __name__ == "__main__":
#     verifica_nota()
#
# import random
#
#
# def joc_ghicit():
#     numar_secret = random.randint(1, 50)
#     incercari = 0
#
#     while True:
#         try:
#             incercare_utilizator = int(input("Ghiceste numarul (1-50): "))
#             incercari += 1
#
#             if incercare_utilizator < 1 or incercare_utilizator > 50:
#                 print("Introdu un numar valid intre 1 și 50.")
#                 continue
#
#             if incercare_utilizator < numar_secret:
#                 print("Numarul este mai mare!")
#             elif incercare_utilizator > numar_secret:
#                 print("Numarul este mai mic!")
#             else:
#                 print(f"Felicitari! Ai ghicit numarul în {incercari} incercari.")
#                 break
#         except ValueError:
#             print("Eroare: Te rog introdu un numar intreg.")
#
#
# if __name__ == "__main__":
#     joc_ghicit()
#
#     import random
#
#
#     def exercitiu_orase():
#         orase = ["București", "Cluj-Napoca", "Timișoara", "Iași"]
#         for index, oras in enumerate(orase, start=1):
#             print(f"{index}. {oras}")
#
#
#     def exercitiu_loterie():
#         print("\nBine ai venit la Loteria Python!")
#         numere_utilizator = []
#         while len(numere_utilizator) < 6:
#             try:
#                 n = int(input(f"Numărul {len(numere_utilizator) + 1}: "))
#                 if 1 <= n <= 49 and n not in numere_utilizator:
#                     numere_utilizator.append(n)
#             except ValueError:
#                 pass
#
#         numere_extrase = random.sample(range(1, 50), 6)
#         ghicite = [n for n in numere_utilizator if n in numere_extrase]
#
#         print(f"Numere extrase: {sorted(numere_extrase)}")
#         print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")
#
#
#     if __name__ == "__main__":
#         # Aici alegi ce funcție să rulezi:
#         exercitiu_orase()
#         exercitiu_loterie()

import random


# def aventura_magica():
#     inventar = []
#     print("--- AVENTURA IN PADUREA MAGICA ---")
#     print("Te trezesti la marginea unei paduri dese. Aerul miroase a pini si magie.")
#
#     directie = input("\nIncotro mergi? (stanga/dreapta): ").lower()
#
#     if directie == "stanga":
#         print("\nMergi spre un rau argintiu. Pe malul apei straluceste ceva.")
#         optiune = input("Cercetezi obiectul sau mergi mai departe? (cercetez/merg): ").lower()
#
#         if optiune == "cercetez":
#             print("Ai gasit o 'Amuleta de Smarald'! A fost adaugata in inventar.")
#             inventar.append("Amuleta de Smarald")
#         else:
#             print("Ai ignorat obiectul si ai dat peste un spiridus morocanos care te-a alungat.")
#
#     elif directie == "dreapta":
#         print("\nTe afunzi in intuneric si dai peste o pestera veche.")
#         optiune = input("Intri in pestera sau urci pe munte? (pestera/munte): ").lower()
#
#         if optiune == "pestera":
#             print("Inauntru ai gasit o 'Sabie de Lumina' veche de secole!")
#             inventar.append("Sabie de Lumina")
#             print("Dar atentie! Un lup paznic s-a trezit.")
#             if "Sabie de Lumina" in inventar:
#                 print("Lupul s-a speriat de lumina sabiei si a fugit.")
#         else:
#             print("Pe munte ai gasit 'Floarea de Gheata'.")
#             inventar.append("Floarea de Gheata")
#     else:
#         print("\nTe-ai ratacit pentru ca nu ai ales o directie valida!")
#
#     print("\n--- SFARSITUL CALATORIEI ---")
#     if inventar:
#         print(f"Ai terminat aventura cu urmatoarele obiecte: {', '.join(inventar)}")
#     else:
#         print("Inventarul tau este gol. Data viitoare fii mai curajos!")
#
#
# if __name__ == "__main__":
#     aventura_magica()






my_list = list(range(0,101,2))
print(my_list)

#cub=[n**3 for n in range(1,11)]
#print(cub)

#list1 = [1,2,3,4,5,9]
#list2 = [3,4,5,6,7,8]

#elemente_comune = list(set(list1) & set(list2))
#print(f"Elemente comune: {elemente_comune}")


#set5 = {n for n in range(0,20,2)}
#print(set5)

#text = "piatra"
#litere_distincte = set(text)
#print(litere_distincte)

# text2 = "ananas mar facultate mouse da"
# filter (len(word) >= 5)
# words = {word for word in text2.split() if len(word)}
# print(words)

#dictionar = {n**2 for n in range(1,11)}
#print(dictionar)















