#!/usr/bin/python3

# ----- FONCTION SANS ARGUMENT -----
def greeting():
    print("--------------------------")
    print("       Hello World        ")
    print("--------------------------")

greeting()

# ----- FONCTION AVEC ARGUMENTS -----
def somme_deux_nombres(num1, num2):
    total = num1 + num2
    print("{} + {} = {}".format(num1, num2, total))

somme_deux_nombres(3, 4)

# ----- FONCTION AVEC UNE VALEUR DE RETOUR -----
def carre(num):
    return num * num

my_num = 3
print(carre(2))
print(carre(my_num))
