-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : mer. 01 jan. 2025 à 08:27
-- Version du serveur : 8.0.40
-- Version de PHP : 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `fitshare_database`
--

-- --------------------------------------------------------

--
-- Structure de la table `category`
--

CREATE TABLE `category` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Athlétisme'),
(3, 'Musculation'),
(2, 'Natation');

-- --------------------------------------------------------

--
-- Structure de la table `comment`
--

CREATE TABLE `comment` (
  `id` int NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `training_id` int NOT NULL,
  `author_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `event`
--

CREATE TABLE `event` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `user_id` int NOT NULL,
  `training_id` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `exercise`
--

CREATE TABLE `exercise` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `id_category` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `exercise`
--

INSERT INTO `exercise` (`id`, `name`, `id_category`) VALUES
(1, 'Squat avec barre', 3),
(2, 'Hip Thrust', 3),
(3, 'Fente avant ou arrière (avec haltères)', 3),
(4, 'Fente avant ou arrière (sans haltères)', 3),
(5, 'Soulevé de terre roumain', 3),
(6, 'Good Mornings', 3),
(7, 'Rowing barre', 3),
(8, 'Rowing haltères', 3),
(9, 'Tractions (supination)', 3),
(10, 'Tractions (pronation)', 3),
(11, 'Tirage horizontal à la poulie', 3),
(12, 'Extension lombaire au sol', 3),
(13, 'Extension lombaire sur un banc', 3),
(14, 'Développé militaire (barre)', 3),
(15, 'Développé militaire (haltères)', 3),
(16, 'Développé Arnold', 3),
(17, 'Curl biceps (barre)', 3),
(18, 'Curl biceps (haltères)', 3),
(19, 'Dips sur barres parallèles', 3),
(20, 'Développé couché avec barre', 3),
(21, 'Développé couché avec haltères', 3),
(22, 'Pompes avec variation', 3),
(23, 'Écarté couché avec haltères', 3),
(24, 'Planche avec variante (gainage dynamique)', 3),
(25, 'Roll-out avec roue abdominale', 3),
(26, 'Suitcase Carry', 3),
(27, 'Russian Twist', 3),
(28, 'Clean and Press', 3),
(29, 'Snatch', 3),
(30, 'Burpees avec haltères', 3),
(31, 'Sprint court (20 à 60 m)', 1),
(32, 'Sprint en montée', 1),
(33, 'Départs arrêtés', 1),
(34, 'Fartlek (vitesse variable)', 1),
(35, 'Sauts de grenouille (frog jumps)', 1),
(36, 'Pas chassés (sur 30 m)', 1),
(37, 'Fractionnés longs (200 à 800 m)', 1),
(38, 'Course continue à allure modérée', 1),
(39, 'Côtes longues (100 à 200 m)', 1),
(40, 'Pyramides (progression/dégression des distances)', 1),
(41, 'Sauts en contrebas (drop jumps)', 1),
(42, 'Bondissements alternés', 1),
(43, 'Lancers de médecine-ball', 1),
(44, 'Sauts sur caissons', 1),
(45, 'Montée de genoux rapide (skipping)', 1),
(46, 'Ladders (échelle de coordination)', 1),
(47, 'Pas croisés latéraux', 1),
(48, 'Slaloms autour de plots', 1),
(49, 'Foulées bondissantes (grands pas)', 1),
(50, 'Sauts à cloche-pied alterné', 1),
(51, 'Drills d\'échauffement dynamique (cercles de jambes/montée de genoux/talons-fesses)', 1),
(52, 'Étirements actifs', 1),
(53, 'Sauts jambes tendues', 1),
(54, 'Haies basses', 1),
(55, 'Sauts verticaux avec balancier des bras', 1),
(56, 'Travail de la foulée sur 10 à 15 m', 1),
(57, 'Poussée de bloc de départ', 1),
(58, 'Relais avec passages du témoin', 1),
(59, 'Courses relais avec obstacles', 1),
(60, 'Parcours variés (cross-training)', 1),
(61, 'Battements avec planche', 2),
(62, 'Crawl avec un seul bras', 2),
(63, 'Pull Buoy (travail des bras uniquement)', 2),
(64, 'Plaquettes aux mains', 2),
(65, 'Dos crawlé jambes seules', 2),
(66, 'Sprint en crawl (25 à 50 m)', 2),
(67, 'Cardio', 3),
(68, 'test', 3),
(69, 'test', 3);

-- --------------------------------------------------------

--
-- Structure de la table `goal`
--

CREATE TABLE `goal` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `goal`
--

INSERT INTO `goal` (`id`, `name`) VALUES
(4, 'Conditionnement physique général'),
(2, 'Perte de graisse'),
(5, 'Préparation spécifique'),
(1, 'Prise de masse musculaire'),
(6, 'Récupération/réhabilitation'),
(3, 'Renforcement musculaire');

-- --------------------------------------------------------

--
-- Structure de la table `training`
--

CREATE TABLE `training` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `difficulty` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `category_id` int NOT NULL,
  `goal_id` int NOT NULL,
  `creator_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `training`
--

INSERT INTO `training` (`id`, `title`, `difficulty`, `description`, `category_id`, `goal_id`, `creator_id`) VALUES
(1, 'Conditionnement physique', 'Facile', 'il faut être régulier', 1, 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `trainingexerciselink`
--

CREATE TABLE `trainingexerciselink` (
  `training_id` int NOT NULL,
  `exercise_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `trainingexerciselink`
--

INSERT INTO `trainingexerciselink` (`training_id`, `exercise_id`) VALUES
(1, 31),
(1, 32);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `hashed_password`) VALUES
(1, 'manda', 'manda@gmail.com', '$2b$12$OBc0naY7UbKX6rd7vzncMe1aGxc/9NhEPlSHeB.RsAIx1Lyt.aaky');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_category_name` (`name`);

--
-- Index pour la table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `training_id` (`training_id`),
  ADD KEY `author_id` (`author_id`);

--
-- Index pour la table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `training_id` (`training_id`);

--
-- Index pour la table `exercise`
--
ALTER TABLE `exercise`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_category` (`id_category`),
  ADD KEY `ix_exercise_name` (`name`);

--
-- Index pour la table `goal`
--
ALTER TABLE `goal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_goal_name` (`name`);

--
-- Index pour la table `training`
--
ALTER TABLE `training`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `goal_id` (`goal_id`),
  ADD KEY `creator_id` (`creator_id`),
  ADD KEY `ix_training_title` (`title`),
  ADD KEY `ix_training_description` (`description`),
  ADD KEY `ix_training_difficulty` (`difficulty`);

--
-- Index pour la table `trainingexerciselink`
--
ALTER TABLE `trainingexerciselink`
  ADD PRIMARY KEY (`training_id`,`exercise_id`),
  ADD KEY `exercise_id` (`exercise_id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_user_username` (`username`),
  ADD UNIQUE KEY `ix_user_email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `category`
--
ALTER TABLE `category`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `event`
--
ALTER TABLE `event`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `exercise`
--
ALTER TABLE `exercise`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT pour la table `goal`
--
ALTER TABLE `goal`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `training`
--
ALTER TABLE `training`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`training_id`) REFERENCES `training` (`id`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`);

--
-- Contraintes pour la table `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `event_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `event_ibfk_2` FOREIGN KEY (`training_id`) REFERENCES `training` (`id`);

--
-- Contraintes pour la table `exercise`
--
ALTER TABLE `exercise`
  ADD CONSTRAINT `exercise_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`);

--
-- Contraintes pour la table `training`
--
ALTER TABLE `training`
  ADD CONSTRAINT `training_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  ADD CONSTRAINT `training_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`),
  ADD CONSTRAINT `training_ibfk_3` FOREIGN KEY (`creator_id`) REFERENCES `user` (`id`);

--
-- Contraintes pour la table `trainingexerciselink`
--
ALTER TABLE `trainingexerciselink`
  ADD CONSTRAINT `trainingexerciselink_ibfk_1` FOREIGN KEY (`training_id`) REFERENCES `training` (`id`),
  ADD CONSTRAINT `trainingexerciselink_ibfk_2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;