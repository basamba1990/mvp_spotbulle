# MVP SpotBulle - Frontend

Ce répertoire contient le frontend de l'application SpotBulle, développé avec React.

## Structure du projet

Le projet a été initialisé avec `create-react-app` et utilise `pnpm` comme gestionnaire de paquets. Il inclut Tailwind CSS, shadcn/ui, Lucide icons et Recharts par défaut.

- `public/`: Contient les fichiers statiques publics, comme `index.html`.
- `src/`: Contient le code source de l'application React.
  - `App.js`: Composant principal de l'application.
  - `index.js`: Point d'entrée JavaScript de l'application.
  - `components/`: Répertoire pour les composants React réutilisables.
    - `ui/`: Composants générés par shadcn/ui (si utilisés).
    - `layout/`: Composants de mise en page (Navbar, Footer, Sidebar, etc.).
    - `auth/`: Composants liés à l'authentification (LoginForm, RegisterForm).
    - `pods/`: Composants pour la gestion et l'affichage des pods.
    - `profile/`: Composants pour l'affichage et la gestion du profil utilisateur (y compris le test DISC).
    - `ia/`: Composants pour interagir avec les modules d'IA (affichage des suggestions de matching, etc.).
  - `pages/`: Répertoire pour les composants de page de haut niveau (correspondant aux routes).
    - `HomePage.js`
    - `LoginPage.js`
    - `RegisterPage.js`
    - `ProfilePage.js`
    - `PodsPage.js`
    - `DashboardPage.js`
  - `contexts/`: Répertoire pour les Contextes React (ex: AuthContext, ProfileContext).
  - `hooks/`: Répertoire pour les hooks personnalisés.
  - `services/`: Répertoire pour les appels API et la logique de service (ex: `authService.js`, `podService.js`).
  - `utils/`: Répertoire pour les fonctions utilitaires.
  - `assets/`: Répertoire pour les images, polices, etc.
  - `config/`: Fichiers de configuration (ex: constantes, configuration API).

## Scripts disponibles

Dans le répertoire du projet, vous pouvez exécuter :

### `pnpm run dev`

Lance l'application en mode développement.
Ouvrez [http://localhost:3000](http://localhost:3000) pour la voir dans votre navigateur.
La page se rechargera si vous faites des modifications.
Vous verrez également les erreurs de lint dans la console.

### `pnpm run build`

Construit l'application pour la production dans le dossier `build`.
Il regroupe correctement React en mode production et optimise la construction pour les meilleures performances.

La construction est minifiée et les noms de fichiers incluent les hachages.
Votre application est prête à être déployée !

## Intégration avec le Backend

Les appels API vers le backend Flask se feront depuis les fichiers dans `src/services/`.
Assurez-vous que le backend Flask est en cours d'exécution et accessible.

## Design et UI

Le prompt mentionne l'utilisation de Figma-to-React ou Locofy. Les composants générés peuvent être intégrés dans la structure `src/components/`.
