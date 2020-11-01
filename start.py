from textwrap import wrap


def format_output(texte, regroupement):
    output = ""
    split = wrap(texte, regroupement)
    for bloc in split:
        output += bloc + " "
    return output


def caesar(texte_clair, decalage):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nb_carac = len(caracteres)
    texte_code = ""
    for car in texte_clair:
        if car != ' ':
            pos = caracteres.find(car)
            pos = (pos + decalage) % nb_carac
            texte_code += caracteres[pos]
    return format_output(texte_code, 5)


def main():
    texte_clair = input("Quel est le texte ? ").upper()
    decalage = int(input("quel est le décalage ?"))
    texte_code = caesar(texte_clair, decalage)
    texte_code_inverse = caesar(texte_clair, -decalage)
    print(f"Texte codé : {texte_code}")
    print(f"Texte inversé : {texte_code_inverse}")


if __name__ == "__main__":
    main()
