🚀 Guide d'installation et de test du projet
Ce projet utilise Docker et Django. Suivez les étapes ci-dessous pour l'installer et le tester.

🛠️ Prérequis
Docker installé sur votre machine
Git installé pour cloner le repository

📥 Étape 1 : Cloner le repository
git clone <URL_DU_REPO>
cd parseur_django

🔥 Étape 2 : Démarrer Docker
Assurez-vous que Docker est bien lancé :
sudo systemctl start docker
sudo systemctl status docker
Si tout est en ordre, vous devriez voir un statut actif.

📂 Étape 3 : Se positionner dans le dossier du projet
cd src

🏗️ Étape 4 : Préparer et lancer le conteneur Docker
docker compose build
docker compose up

📌 Remarque : Le service container_parseur_app peut prendre un peu de temps à démarrer.

🎉 Félicitations ! Votre projet est prêt à être utilisé.

🧪 Étape 5 : Tester le projet
Rendez-vous sur l'URL suivante :
👉 http://localhost:8000/display/audits/

Téléchargez les deux fichiers situés dans le dossier exemple_docs_a_telecharger.
Uploadez ces fichiers pour tester le parseur de PDF.


