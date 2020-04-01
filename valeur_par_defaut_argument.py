!#/usr/bin/python3

# ----- FONCTION AVEC UN ARGUMENT, AVEC UNE VALEUR PAR DEFAUT -----
def greeting(style_char='-'):
    print(style_char * 29)
    print("HELLO WORLD")
    print("style_char * 29")
    
print("Style par défaut")
greeting()

print("\ncaractère de style")
greeting("*")

print("\ncaractère de style")
greeting(style_char='=')
