from operator import xor

def Pivot61_a_gauche(cle):
    """
    Pivote une liste de 61 positions vers la gauche

    Param:
        - cle (list): la liste a pivoter

    Retour:
        - nouvelle_cle (list): Le résultat du pivot de la liste en entrée
    """
    tmp = cle[61:80]
    nouvelle_cle = tmp + cle[0:61]
    return nouvelle_cle

def Permutation(Etat):
    """
    Effectue une permutation bit_a_bit sur une liste selon P

    Param:
        - Etat (list): La liste a permutée

    Retour:
        - nouvel_Etat (list): Le résultat de la permutation de la liste en entrée

    """
    P = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]
    
    nouvel_Etat = [None] * len(Etat)
    for i, p in enumerate(P):
        nouvel_Etat[p] = Etat[i]
    return nouvel_Etat

def Boite_s(_4bits):
    """
    Implémentation de la boite S
    Param:
        - _4bits(int représente 4 bits): le nombre en entrée de la boite S

    Retour: 
        - resultat(str représente 4 bits): le resultat de la substitution du nombre _4bits
    """
    # Initialisation du tableau de substitution
    S = {
        '0x0': '0xc',
        '0x1': '0x5',
        '0x2': '0x6',
        '0x3': '0xb',
        '0x4': '0x9',
        '0x5': '0x0',
        '0x6': '0xa',
        '0x7': '0xd',
        '0x8': '0x3',
        '0x9': '0xe',
        '0xa': '0xf',
        '0xb': '0x8',
        '0xc': '0x4',
        '0xd': '0x7',
        '0xe': '0x1',
        '0xf': '0x2',
    }
    _4bits = hex(int(str(_4bits), 2))
    for j in S.keys():
        if j == _4bits:
            resultat = S[j] 
            break
    resultat = format(int(resultat, 16), "b")
    return resultat

def Substitution(Etat_en_binaire):
    """
    Effectue des changements sur une liste selon la boite_s

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
        tmp = Boite_s(Etat_en_hexa[i])
        if len(tmp) == 4:
            for bit in tmp:
                nouvel_Etat.append(int(bit))
        else:
            for _ in range(4-len(tmp)):
                nouvel_Etat.append(0)
            for bit in tmp:
                nouvel_Etat.append(int(bit))
    return nouvel_Etat
 
def Cadencement_de_cle (cle_maitre):
    for _ in range(56):
        cle_maitre.append(0)
    sous_cle = []
    # Ki = K40 k41 ... K62 K63
    for i in range(1, 12):
        binaire = 0
        sous_cle.append(cle_maitre[40:64])
        cle_maitre = Pivot61_a_gauche(cle_maitre)
        for j in range(4):
            binaire = binaire*10 + cle_maitre[j] 
        tmp = Boite_s(binaire)
        _4bits = []
        if len(tmp) == 4:
            for ele in tmp:
                _4bits.append(int(ele))
        else:
            for _ in range(4-len(tmp)):
                _4bits.append(0)
            for ele in tmp:
                _4bits.append(int(ele))
        cle_maitre[0:4] = _4bits
        #60 ... 65
        ##############################
        i_binaire = bin(i)
        i_binaire = i_binaire[2:]
        liste = []
        if len(i_binaire) == 5:
            for ele in i_binaire:
                liste.append(int(ele))
        else:
            for _ in range(5-len(i_binaire)):
                liste.append(0)
            for ele in i_binaire:
                liste.append(int(ele))
        indice = 60
        for k in range(5):
            cle_maitre[indice+k] = xor(cle_maitre[indice+k], liste[k])
        # Affichage des sous clés
        #print(sous_cle[i-1])
    return sous_cle

def Chiffrement(Etat, cle_maitre):
    """
    Chiffre le message (Etat) par la clé (cle_maitre)

    Param:
        - Etat(list)       : Le message claire
        - cle_maitre (list): La clé du chiffrement

    Retour: 
        - Etat(list): Le message chiffré
    """
    sous_cle = Cadencement_de_cle(cle_maitre)

    for j in range(10):
        for i in range(24):
            Etat[i] = xor(Etat[i], sous_cle[j][i])
        Etat = Substitution(Etat)
        Etat = Permutation(Etat)
    binaire     = 0
    cpt         = 0
    nouvel_Etat = []
    for i in range(24):
        Etat[i] = xor(Etat[i], sous_cle[10][i])
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