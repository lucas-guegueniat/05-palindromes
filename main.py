"""
Lucas Guéguéniat - 05-palindromes
"""

import unicodedata

def ispalindrome(p):
    """
    Vérifie si la suite de caractères prise en argument est un palindrome.
    """
    m = ""
    n = ""
    if p == p[::-1]:
        return True
    for i in p:
        if i not in (' ', ',', ':', "'", '!', '?', '-', ';', '_'):
            m = m + i.lower()
    x = unicodedata.normalize('NFD', m)
    res = ''.join([c for c in x if not unicodedata.combining(c)])
    for i in p[::-1]:
        if i not in (' ', ',', ':', "'", '!', '?', '-', ';', '_'):
            n = n + i.lower()
    y = unicodedata.normalize('NFD', n)
    rep = ''.join([c for c in y if not unicodedata.combining(c)])
    if res == rep:
        return True
    return False

#### Fonction principale


def main():
    """
    Teste la fonction secondaire ci-dessus pour s'assurer qu'elle fonctionne.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
