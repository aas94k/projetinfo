def demander_nombre(message, min_val=None, max_val=None):

    while True:
        s = input(message).strip()
        if s == "":
            print("Veuillez entrer un nombre valide.")
            continue
        if s[0] == '-':
            if len(s) == 1:  # pas de chiffres après le signe "-"
                print("Veuillez entrer un nombre valide.")
                continue
            digits = s[1:]
            sign = -1
        else:
            digits = s
            sign = 1
        if not all('0' <= c <= '9' for c in digits):
            print("Veuillez entrer un nombre entier.")
            continue
        valeur = 0
        for c in digits:
            valeur = valeur * 10 + (ord(c) - ord('0'))
        valeur *= sign
        if min_val is not None and valeur < min_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue
        if max_val is not None and valeur > max_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue
    return valeur


choix = demander_nombre("Niveau de courage (1-10) : ", 1, 10)