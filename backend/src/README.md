# MVP SpotBulle - Backend

Ce répertoire contient le backend de l'application SpotBulle, développé avec Flask.

## Structure du projet

- `src/`: Contient le code source de l'application.
  - `main.py`: Point d'entrée principal de l'application Flask.
  - `models/`: Contient les modèles de données SQLAlchemy.
    - `user.py`: Modèle pour les utilisateurs.
    - `profile.py`: Modèle pour les profils DISC et autres informations de profil.
    - `pod.py`: Modèle pour les pods d'entraide.
  - `routes/`: Contient les blueprints pour les différentes routes de l'API.
    - `auth.py`: Routes pour l'authentification.
    - `users.py`: Routes pour la gestion des utilisateurs.
    - `profiles.py`: Routes pour la gestion des profils.
    - `pods.py`: Routes pour la gestion des pods.
    - `ia_modules.py`: Routes pour les interactions avec les modules IA.
  - `services/`: Contient la logique métier et les services.
    - `disc_service.py`: Logique liée au profilage DISC.
    - `matching_service.py`: Logique pour le matching IA.
  - `utils/`: Contient des fonctions utilitaires.
- `venv/`: Environnement virtuel Python.
- `requirements.txt`: Liste des dépendances Python.
- `migrations/`: Contient les migrations de base de données Alembic (si Flask-Migrate est utilisé).

## Démarrage

1.  Assurez-vous que Python 3.11+ et pip sont installés.
2.  Créez et activez un environnement virtuel :
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```
3.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
4.  Configurez les variables d'environnement nécessaires (ex: `DATABASE_URL`, clés API pour l'IA) dans un fichier `.env`.
5.  Lancez l'application :
    ```bash
    flask run
    ```

## Modules IA

Les emplacements pour l'intégration des modules IA (ex: LLM, classification DISC, matching) sont prévus dans `src/services/` et les routes correspondantes dans `src/routes/ia_modules.py`.
