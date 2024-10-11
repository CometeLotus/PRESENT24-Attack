from operator import xor
from CHIFFREMENT import Cadencement_de_cle
from CHIFFREMENT import Chiffrement


def INV_Permutation(Etat):
    """
    P: une liste représentant la permutation à inverser

    n: la longueur de la permutation (par défaut 24)

    Retourne la liste inversée de la permutation P.
    """
    P = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]
    nouvel_Etat = [0 for _ in range(24)]
    for i,j in enumerate(P):
        nouvel_Etat[i] = Etat[j]
    return nouvel_Etat

def INV_Boite_s(_4bits):
    """
    Implémentation de l'inverse de la boite S
    Param:
        - 4bits(int représente 4 bits): le nombre en entrée de la boite S

    Retour: 
        - resultat(str représente 4 bits): le resultat de la substitution du nombre 4bits
    """
    # Initialisation du tableau de substitution
    S = {
        '0xc': '0x0',
        '0x5': '0x1',
        '0x6': '0x2',
        '0xb': '0x3',
        '0x9': '0x4',
        '0x0': '0x5',
        '0xa': '0x6',
        '0xd': '0x7',
        '0x3': '0x8',
        '0xe': '0x9',
        '0xf': '0xa',
        '0x8': '0xb',
        '0x4': '0xc',
        '0x7': '0xd',
        '0x1': '0xe',
        '0x2': '0xf',
    }
    _4bits = hex(int(str(_4bits), 2))
    for j in S.keys():
        if j == _4bits:
            resultat = S[j] 
            break
    resultat = format(int(resultat, 16), "b")
    return resultat

def INV_Substitution(Etat_en_binaire):
    """
    Effectue des changements sur une liste selon la INV_Boite_s

    Param:
        - Etat (list): La liste a changer

    Retour: 
        - nouvel_Etat (list): Le résultat du chngement de la liste en entrée
    """
    binaire = 0
    cpt     = 0
    Etat_en_hexa = []
    for i in range(24):
        if cpt < 4:
            binaire = binaire*10 + Etat_en_binaire[i] 
            cpt    += 1
        else:
            Etat_en_hexa.append(binaire)
            cpt     = 0
            binaire = 0
            binaire = binaire*10 + Etat_en_binaire[i] 
            cpt    += 1
    Etat_en_hexa.append(binaire)
    
    tmp = ""
    nouvel_Etat = []
    for i in range(6): 
        tmp = INV_Boite_s(Etat_en_hexa[i])
        if len(tmp) == 4:
            for bit in tmp:
                nouvel_Etat.append(int(bit))
        else:
            for _ in range(4-len(tmp)):
                nouvel_Etat.append(0)
            for bit in tmp:
                nouvel_Etat.append(int(bit))
    return nouvel_Etat

def Dechiffrement(Etat, cle):
    sous_cle = Cadencement_de_cle(cle)
    for i in range(24):
        Etat[i] = xor(Etat[i], sous_cle[10][i])
    for j in range(10):
        Etat = INV_Permutation(Etat)
        Etat = INV_Substitution(Etat)
        for i in range(24):
            Etat[i] = xor(Etat[i], sous_cle[9-j][i])
    binaire     = 0
    cpt         = 0
    nouvel_Etat = []
    for i in range(24):
        if cpt < 4:
            binaire = binaire*10 + Etat[i]
            cpt += 1
        else:
            nouvel_Etat.append(binaire)
            cpt = 0
            binaire = 0
            binaire = binaire*10 + Etat[i]
            cpt += 1
    nouvel_Etat.append(binaire)
    tmp = ""
    for i in range(6):
        tmp += hex(int(str(nouvel_Etat[i]), 2))[2:]
    return tmp


print("##### PRESENT24 #####")
choix = input("- Tapez 1 pour faire un chiffrement.\n- Tapez 2 pour faire un déchiffrement.\n")
while True:
    if choix == '1':
        # Récupération du message claire et le convertire en binaire
        message   = input("Entrez votre message clair (en héxadécimal):\n")
        message   = int(message, 16)
        message   = format(message, "b")
        Etat      = [int(ele) for ele in message]
        long_Etat = len(Etat)
        if long_Etat != 24:
            liste = [0 for _ in range(24-long_Etat)]
            Etat = liste + Etat
        # Récupération de la clé maitre et la convertire en binaire
        print("")
        tmp        = input("Entrez votre clé (en héxadécimal):\n")
        tmp        = int(tmp, 16)
        tmp        = list(format(tmp, "b"))
        cle_maitre = [int(ele) for ele in tmp]
        long_cle   = len(cle_maitre)
        if long_cle != 24:
            liste = [0 for _ in range(24-long_cle)]
            cle_maitre = liste + cle_maitre
        print("")
        print("Le message chiffré est: {}\n".format(Chiffrement(Etat, cle_maitre)))
        break
    elif choix == '2':
        # Récupération du message claire et le convertire en binaire
        message   = input("Entrez votre message chiffré (en héxadécimal):\n")
        message   = int(message, 16)
        message   = format(message, "b")
        Etat      = [int(ele) for ele in message]
        long_Etat = len(Etat)
        if long_Etat != 24:
            liste = [0 for _ in range(24-long_Etat)]
            Etat = liste + Etat
        # Récupération de la clé maitre et la convertire en binaire
        print("")
        tmp        = input("Entrez votre clé (en héxadécimal):\n")
        tmp        = int(tmp, 16)
        tmp        = list(format(tmp, "b"))
        cle_maitre = [int(ele) for ele in tmp]
        long_cle   = len(cle_maitre)
        if long_cle != 24:
            liste = [0 for _ in range(24-long_cle)]
            cle_maitre = liste + cle_maitre
        print("")
        print("Le message clair est: {}\n".format(Dechiffrement(Etat, cle_maitre)))
        break
    else:
        choix = input("Saisie incorrecte, réessayer.\n")