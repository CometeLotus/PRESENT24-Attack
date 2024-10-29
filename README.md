# Projet de Chiffrement et Attaque PRESENT24

## Description

Ce projet implémente le chiffrement et le déchiffrement à l'aide de l'algorithme PRESENT24. Il contient trois fichiers principaux : `Chiffrement.py`, `Dechiffrement.py`, et `attaque.py`. Le projet permet de chiffrer un message clair avec une clé, de le déchiffrer et d'effectuer des attaques sur le chiffrement.

## Fonctionnalités
- **Chiffrement** : Chiffrement d'un message clair en utilisant une clé fournie.
- **Déchiffrement** : Déchiffrement d'un message chiffré en utilisant la même clé.
- **Attaque** : Attaque par le milieu sur ce chiffrement pour retrouver la clé a partir d'un couple clair/chiffré. 

## Utilisation
### Prérequis
- Python 3.x (pour vérifier, exécutez `python --version`)

## Structure du projet

- `main.py` : Fichier principal exécutant le script de chiffrement et déchiffrement.
- `Chiffrement.py` : Contient les fonctions de chiffrement et de génération de sous-clés.
- `Dechiffrement.py` : Contient les fonctions de déchiffrement et les fonctions inverses de permutation et substitution.
- `Attaque.py` : Contient la logique de l'attaque par le milieu.
- `Present24.pdf`: Documentation détaillée du chiffrement PRESENT24 ainsi que de l'attaque par le milieu.

## Dépendances

Ce projet utilise les bibliothèques suivantes :
- `itertools` : Permet de générer toutes les combinaisons possibles de bits pour une clé donnée.
- `from operator import xor` : Permet d’utiliser la fonction xor pour effectuer une opération de XOR bit-à-bit.

Assurez-vous d'avoir installé ces bibliothèques avant d'exécuter le projet. Vous pouvez les installer en utilisant pip :

```sh
pip install itertools operator
```

## Utilisation

1. Exécutez `main.py` avec la commande suivante :

    ```bash
    python main.py
    ```

2. Suivez les instructions à l'écran :
    - **Tapez `1` pour chiffrer un message** : Entrez le message clair (en hexadécimal) et la clé.
    - **Tapez `2` pour déchiffrer un message** : Entrez le message chiffré (en hexadécimal) et la clé.

## Exemple de fonctionnement

```plaintext
##### PRESENT24 #####
- Tapez 1 pour faire un chiffrement.
- Tapez 2 pour faire un déchiffrement.
1
Entrez votre message clair (en héxadécimal) :
123abc
Entrez votre clé (en héxadécimal) :
456def

Le message chiffré est : b0402b
```

## Documentation

Pour une compréhension détaillée de l’algorithme PRESENT24 et de l’attaque Meet-in-the-Middle, référez-vous à `Present24.pdf` fourni dans le dépôt.
