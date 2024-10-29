from CHIFFREMENT import Chiffrement
from DECHIFFREMENT import Dechiffrement

def hex_to_bin_array(hex_input, bit_length=24):
    """Convertit une chaîne hexadécimale en tableau de bits binaire de longueur spécifiée."""
    binary_string = bin(int(hex_input, 16))[2:].zfill(bit_length)
    return [int(bit) for bit in binary_string]

def input_hexadecimal(prompt):
    """Demande une saisie hexadécimale à l'utilisateur et vérifie sa validité."""
    while True:
        hex_input = input(prompt)
        try:
            # Test de conversion en entier base 16 pour vérifier le format hexadécimal
            int(hex_input, 16)
            return hex_input  # Retourne l'entrée valide
        except ValueError:
            print("Erreur : Veuillez entrer une valeur hexadécimale valide.")

def main():
    print("##### PRESENT24 #####")
    while True:
        choix = input("- Tapez 1 pour faire un chiffrement.\n- Tapez 2 pour faire un déchiffrement.\n")
        if choix in ['1', '2']:
            # Récupération et conversion du message
            message_hex = input_hexadecimal("Entrez votre message {} (en héxadécimal) :\n".format(
                "clair" if choix == '1' else "chiffré"
            ))
            Etat = hex_to_bin_array(message_hex)
            
            # Récupération et conversion de la clé
            cle_hex = input_hexadecimal("Entrez votre clé (en héxadécimal) :\n")
            cle_maitre = hex_to_bin_array(cle_hex)

            # Exécution du chiffrement ou déchiffrement
            if choix == '1':
                print("\nLe message chiffré est : {}\n".format(Chiffrement(Etat, cle_maitre)))
            else:
                print("\nLe message clair est : {}\n".format(Dechiffrement(Etat, cle_maitre)))
            break
        else:
            print("Saisie incorrecte, veuillez réessayer.\n")

if __name__ == "__main__":
    main()
