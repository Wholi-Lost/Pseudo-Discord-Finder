# Bot Discord - Historique des Pseudos

## Description

Ce bot Discord permet de suivre les anciens pseudos des membres d'un serveur. Lorsqu'un utilisateur change son pseudo, l'ancien est sauvegardé dans un fichier JSON. Grâce à une commande dédiée, les utilisateurs peuvent consulter leur dernier pseudo enregistré.

## Fonctionnalités

- **Suivi automatique des pseudos** : Capture et stocke les anciens pseudos des membres.
- **Consultation des anciens pseudos** : Permet aux utilisateurs de voir leur dernier pseudo enregistré avec la commande `!look`.

## Prérequis

Avant de lancer le bot, assurez-vous d'avoir installé :

- Python 3.x
- La bibliothèque `discord.py`

Installation de `discord.py` :

```bash
pip install discord
```

## Installation et Configuration

1. **Clonez ou téléchargez** ce projet.
2. **Ajoutez votre Token Discord** dans le fichier `script.py` :
   - Remplacez `TOKEN = ""` par votre token de bot Discord.
3. **Lancez le bot** avec la commande :
   ```bash
   python script.py
   ```

## Fichiers

- `script.py` : Code source du bot.
- `pseudos.json` : Fichier où sont enregistrés les anciens pseudos.

## Utilisation

- **Démarrer le bot** : Exécutez le script avec Python.
- **Commandes disponibles** :
  - `!look` : Permet à un utilisateur de voir son dernier pseudo enregistré.

## Permissions Requises

Le bot doit avoir les permissions suivantes sur le serveur Discord :

- Gérer les pseudos (`Manage Nicknames`)
- Lire les messages (`Read Messages`)
- Envoyer des messages (`Send Messages`)

## Contributions

Les contributions sont les bienvenues ! Vous pouvez proposer des améliorations via des pull requests.

## Licence

Ce projet est sous licence lost/woly. Vous êtes libre de le modifier et de le redistribuer.

