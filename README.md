## English
___
# Encrypted Safe

Secure your sensitive data with `Encrypted Safe`, an intuitive encryption tool designed to protect personal and commercial information through robust file and folder encryption.

## Key Features

- **Data Encryption**: Encrypt files and folders with a strong encryption key.
- **Secure Data Transfer**: Encrypt files before sending them electronically, ensuring that only the intended recipient can decrypt them.
- **Long-term Secure Storage**: Encrypt entire volumes or large datasets for secure long-term storage.
- **Secure Data Deletion**: Securely delete files to prevent potential recovery.

## Getting Started

### Prerequisites

- Python 3.8 or later
- PyQt5
- Cryptography library

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Tom-Souillard/encrypted_safe.git
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python main.py
   ```
   Follow the on-screen instructions to select files for encryption or decryption.

### Docker Usage

To build and run the application using Docker:

```bash
docker build -t encrypted_safe .
docker run -d -p 5000:5000 encrypted_safe
```

### Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

### Contact

If you have any questions, please open an issue in the GitHub repository.

---

## Français

# EncryptedSafe

EncryptedSafe est un outil robuste de chiffrement de fichiers et de dossiers, conçu pour fournir aux particuliers et aux petites entreprises des méthodes sécurisées pour protéger, transférer et stocker des données sensibles. Ce projet utilise Python et PyQt pour offrir une expérience utilisateur conviviale sur plusieurs plateformes.

## Fonctionnalités Clés

- **Chiffrement de données** : Chiffrement simple et sécurisé de fichiers et dossiers sélectionnés avec des clés de chiffrement fortes.
- **Transfert sécurisé de données** : Intègre une fonction d'exportation qui chiffre les fichiers avant leur envoi, assurant que seuls les destinataires prévus puissent les déchiffrer.
- **Stockage sécurisé à long terme** : Chiffre des volumes entiers ou de grands ensembles de données avec des fonctionnalités de gestion de clés pour une sécurité prolongée.
- **Suppression sécurisée de données** : Intègre une fonction de suppression sécurisée pour effacer de manière irréversible les fichiers après chiffrement ou lorsqu'ils ne sont plus nécessaires.

## Pour Commencer

### Prérequis

- Python 3.8+
- PyQt5
- Bibliothèque Cryptography

### Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Tom-Souillard/encrypted_safe.git
   ```
2. **Configurer un environnement virtuel** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows utilisez `venv\Scripts\activate`
   ```
3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
4. **Exécuter l'application** :
   ```bash
   python main.py
   ```
   Suivez les instructions à l'écran pour sélectionner les fichiers à chiffrer ou déchiffrer.

### Utilisation avec Docker

Pour construire et exécuter l'application avec Docker :

```bash
docker build -t encrypted_safe .
docker run -d -p 5000:5000 encrypted_safe
```

### Contribution

Les contributions sont les bienvenues ! Pour les changements importants, veuillez ouvrir une issue d'abord pour discuter de ce que vous aimeriez modifier.

### Licence
Ce projet est sous licence Apache Licence 2.0 - voir le fichier LICENSE pour plus de détails.

### Contact

Si vous avez des questions, veuillez ouvrir une issue dans le dépôt GitHub.