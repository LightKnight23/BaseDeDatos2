# BaseDeDatos2
# Estudiantes: 
# ______________________________
# Alejandro Moreno Eyvar Garcia
# ______________________________
# Taller de Pre-Parcial

CREATE SCHEMA `ElectronicWallet`;
USE `ElectronicWallet`;
CREATE TABLE `User` (
    `user_id` INT PRIMARY KEY,
    `password` VARCHAR(100),
    `salt` VARCHAR(100),
    `status` VARCHAR(50),
    `timestamp` TIMESTAMP,
    `phone` VARCHAR(20),
    `image` VARCHAR(200),
    `aadhar_doc` VARCHAR(200)
);

INSERT INTO `User` (`user_id`, `password`, `salt`, `status`, `timestamp`, `phone`, `image`, `aadhar_doc`)
VALUES (1, 'password1', 'salts1', 'active', NOW(), '1234567890', 'image1.jpg', 'aadhar1.jpg'),
       (2, 'password2', 'salts2', 'inactive', NOW(), '2345678901', 'image2.jpg', 'aadhar2.jpg'),
       (3, 'password3', 'salts3', 'active', NOW(), '3456789012', 'image3.jpg', 'aadhar3.jpg'),
       (4, 'password4', 'salts4', 'inactive', NOW(), '4567890123', 'image4.jpg', 'aadhar4.jpg'),
       (5, 'password5', 'salts5', 'active', NOW(), '5678901234', 'image5.jpg', 'aadhar5.jpg');

CREATE TABLE `Contact` (
    `contact_id` INT PRIMARY KEY,
    `user_id` INT,
    `name` VARCHAR(100),
    `reason` VARCHAR(200),
    FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
);

INSERT INTO `Contact` (`contact_id`, `user_id`, `name`, `reason`)
VALUES (1, 1, 'John Doe', 'Friendship'),
       (2, 2, 'Jane Smith', 'Work'),
       (3, 3, 'Alice Johnson', 'School'),
       (4, 4, 'Bob Brown', 'Sports'),
       (5, 5, 'Charlie Green', 'Neighbor');

CREATE TABLE `Friend` (
    `friend_id` INT PRIMARY KEY,
    `user_id` INT,
    `friend_id` INT,
    FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`),
    FOREIGN KEY (`friend_id`) REFERENCES `User`(`user_id`)
);

INSERT INTO `Friend` (`friend_id`, `user_id`, `friend_id`)
VALUES (1, 1, 2),
       (2, 2, 1),
       (3, 3, 4),
       (4, 4, 3),
       (5, 5, 1);

CREATE TABLE `Request` (
    `request_id` INT PRIMARY KEY,
    `from_id` INT,
    `to_id` INT,
    `status` VARCHAR(50),
    `timestamp` TIMESTAMP,
    `category` VARCHAR(50),
    `balance` DECIMAL(10, 2),
    FOREIGN KEY (`from_id`) REFERENCES `User`(`user_id`),
    FOREIGN KEY (`to_id`) REFERENCES `User`(`user_id`)
);

INSERT INTO `Request` (`request_id`, `from_id`, `to_id`, `status`, `timestamp`, `category`, `balance`)
VALUES (1, 1, 3, 'pending', NOW(), 'loan', 500.00),
       (2, 2, 4, 'approved', NOW(), 'transfer', 200.00),
       (3, 3, 5, 'rejected', NOW(), 'loan', 1000);


# Diagrama
# ____________________________________________________________________________________

<img width="985" alt="Screenshot 2024-02-22 at 7 18 50 PM" src="https://github.com/LightKnight23/BaseDeDatos2/assets/42986343/9baf1ce9-2514-4343-be77-f7305c71ece8">
