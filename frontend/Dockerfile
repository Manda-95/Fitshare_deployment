# Utiliser une image officielle Node.js
FROM node:18-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour les dépendances
COPY package.json package-lock.json ./

# Nettoyer le cache npm et installer les dépendances
RUN npm cache clean --force && npm install --legacy-peer-deps

# Ajouter le dossier des binaires Node.js au PATH

# Copier tout le reste des fichiers
COPY . .

# Exposer le port de Vite
EXPOSE 5173

# Commande par défaut pour démarrer le serveur de développement
CMD ["npm", "run", "dev", "--", "--host"]
