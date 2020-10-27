from textwrap import wrap

def formatOutput(texte, regroupement):
    output = ""
    split = wrap(texte, regroupement)
    for bloc in split:
        output += bloc + " "
    return output

def caesar(texteClair, decalage):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nbCarac = len(caracteres)
    texteCode = ""
    for car in texteClair:
        if car != ' ':
            pos = caracteres.find(car)
            pos = (pos + decalage) % nbCarac
            texteCode += caracteres[pos]
    return formatOutput(texteCode, 5)

def main():
    texteClair = input("Quel est le texte ? ").upper()
    decalage = int(input("quel est le décalage ?"))
    texteCode = caesar(texteClair, decalage)
    print(f"Texte codé : {texteCode}")

if __name__ == "__main__":
    main()