## English
___
# encrypted_safe

**encrypted_safe** is a comprehensive password management application that provides robust security features such as custom encryption algorithms, user account management via a Tkinter interface, and file operations within the Windows environment. It ensures high-security standards and comes equipped with detailed activity logging capabilities to maintain a secure and reliable user experience.

### Features

- **Custom encryption**: Utilizes a unique encryption mechanism for password security.
- **User Account Management**: Allows users to create, manage, and authenticate user accounts.
- **File Management**: Enables manipulation of files and directories on Windows.
- **Logging**: Tracks user activities with detailed logs for auditing and security purposes.

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

### Docker Usage

To build and run the application using Docker:

```bash
docker build -t encrypted_safe .
docker run -d -p 5000:5000 encrypted_safe
```

### Contributing

Contributions are welcome! Please refer to CONTRIBUTING.md for more information on how to contribute to this project.

### License
This project is licensed under the Apache License - see the LICENSE.md file for details.

---

## Français

# encrypted_safe

**encrypted_safe** est une application complète de gestion de mots de passe offrant de robustes fonctionnalités de sécurité telles que des algorithmes de chiffrement personnalisés, la gestion des comptes utilisateurs via une interface Tkinter, et la manipulation de fichiers dans l'environnement Windows. Elle garantit des normes de sécurité élevées et est équipée de capacités détaillées de journalisation des activités pour maintenir une expérience utilisateur sécurisée et fiable.

### Fonctionnalités

- **Chiffrement personnalisé** : Utilise un mécanisme de chiffrement unique pour la sécurité des mots de passe.
- **Gestion des comptes utilisateurs** : Permet aux utilisateurs de créer, gérer et authentifier les comptes.
- **Gestion de fichiers** : Permet la manipulation des fichiers et répertoires sous Windows.
- **Journalisation** : Suit les activités des utilisateurs avec des logs détaillés pour l'audit et la sécurité.

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

### Utilisation avec Docker

Pour construire et exécuter l'application avec Docker :

```bash
docker build -t encrypted_safe .
docker run -d -p 5000:5000 encrypted_safe
```

### Contribution

Les contributions sont les bienvenues ! Veuillez consulter le fichier CONTRIBUTING.md pour plus d'informations sur comment contribuer à ce projet.

### Licence
Ce projet est sous Apache License - voir le fichier LICENSE.md pour les détails.
