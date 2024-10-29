from operator import xor
from CHIFFREMENT import Cadencement_de_cle

def INV_Permutation(Etat):
    """
    Applique l'inverse de la permutation P à l'état donné.
    """
    P = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]
    return [Etat[j] for j in P]

def INV_Boite_s(bits4):
    """
    Applique la substitution inverse de la boîte S pour un bloc de 4 bits.
    """
    S = {
        '0xc': '0x0', '0x5': '0x1', '0x6': '0x2', '0xb': '0x3', 
        '0x9': '0x4', '0x0': '0x5', '0xa': '0x6', '0xd': '0x7',
        '0x3': '0x8', '0xe': '0x9', '0xf': '0xa', '0x8': '0xb', 
        '0x4': '0xc', '0x7': '0xd', '0x1': '0xe', '0x2': '0xf'
    }
    bits4_hex = hex(int(str(bits4), 2))
    result_hex = S.get(bits4_hex, '0x0')
    return format(int(result_hex, 16), '04b')

def INV_Substitution(Etat_binaire):
    """
    Applique la substitution inverse sur des blocs de 4 bits dans l'état binaire donné.
    """
    # Conversion de l'état en blocs de 4 bits pour l'application de la boîte S inverse
    blocs_4bits = [Etat_binaire[i:i+4] for i in range(0, len(Etat_binaire), 4)]
    nouvel_Etat = []

    for bloc in blocs_4bits:
        bits = ''.join(map(str, bloc))
        nouveau_bloc = INV_Boite_s(bits)
        nouvel_Etat.extend(int(bit) for bit in nouveau_bloc.zfill(4))
    
    return nouvel_Etat

def Etat_to_hex_string(Etat):
    """
    Convertit un état binaire de 24 bits en une chaîne hexadécimale.
    """
    blocs_4bits = [Etat[i:i+4] for i in range(0, len(Etat), 4)]
    hex_string = ''.join(hex(int(''.join(map(str, bloc)), 2))[2:] for bloc in blocs_4bits)
    return hex_string

def Dechiffrement(Etat, cle):
    """
    Déchiffre un message en appliquant l'inverse du chiffrement PRESENT24.
    """
    sous_cles = Cadencement_de_cle(cle)

    # Application de la clé de fin de chiffrement
    Etat = [xor(Etat[i], sous_cles[10][i]) for i in range(24)]

    # Boucle de déchiffrement
    for tour in range(10):
        Etat = INV_Permutation(Etat)
        Etat = INV_Substitution(Etat)
        Etat = [xor(Etat[i], sous_cles[9-tour][i]) for i in range(24)]
    
    # Conversion finale en hexadécimal
    return Etat_to_hex_string(Etat)
