# Base De Datos 2
# Estudiantes: 
# ________________________________
# Alejandro Moreno, Eyvar Garcia
# ________________________________
# Taller de Pre-Parcial

#Problema 1

```sql
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

```
# Diagrama
# _______________________________________________________

<img width="985" alt="Screenshot 2024-02-22 at 7 18 50 PM" src="https://github.com/LightKnight23/BaseDeDatos2/assets/42986343/9baf1ce9-2514-4343-be77-f7305c71ece8">


# Problema 2

```sql
CREATE SCHEMA `Expedientes`;
USE `Expedientes`;
# Crear tabla de Usuarios para la pantalla de inicio de sesión
CREATE TABLE Usuarios (
    IDUsuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NombreUsuario VARCHAR(50) NOT NULL,
    Contraseña VARCHAR(50) NOT NULL
);

CREATE TABLE Aseguradora (
    IDAseguradora INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(200),
    Telefono VARCHAR(20)
);

CREATE TABLE Expedientes (
    IDExpediente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    IDAseguradora INT,
    IDUsuario INT,
    FechaInicio DATE,
    Descripcion TEXT,
    FOREIGN KEY (IDAseguradora) REFERENCES Aseguradora(IDAseguradora),
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);

CREATE TABLE Reportes (
    IDReporte INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    IDExpediente INT,
    FechaReporte DATE,
    Descripcion TEXT,
    FOREIGN KEY (IDExpediente) REFERENCES Expedientes(IDExpediente)
);

CREATE TABLE Juzgado (
    IDJuzgado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(200),
    Telefono VARCHAR(20)
);

INSERT INTO Aseguradora (Nombre, Direccion, Telefono) VALUES
    ('ASSA', '123 Calle Ficticia, Ciudad Ficticia', '+123 456 7890'),
    ('ANCON', '456 Avenida Imaginaria, Pueblo Irreal', '+234 567 8901'),
    ('CONANCE', '789 Calle de Ensueño, Villa Irrealidad', '+345 678 9012'),
    ('PARTICULAR', '321 Boulevard de los Sueños, Ciudad de los Deseos', '+456 789 0123'),
    ('INTEROCEANICA', '654 Carrera Imaginativa, Metrópolis Fantástica', '+567 890 1234');

INSERT INTO Usuarios (NombreUsuario, Contraseña) VALUES
    ('Anthony Trejos', 'contrasena1'),
    ('Luis Molina', 'contrasena2'),
    ('Katherine Kent', 'contrasena3'),
    ('Martin Alvarado', 'contrasena4'),
    ('Candice Henry', 'contrasena5');

INSERT INTO Juzgado (Nombre, Direccion, Telefono) VALUES
    ('Juzgado 5to', '555 Plaza Judicial, Ciudad Judicial', '+111 222 3333'),
    ('Juzgado 4to', '444 Corte de Justicia, Pueblo Legal', '+222 333 4444'),
    ('Juzgado 1ro', '111 Calle Legalidad, Metrópolis Legal', '+333 444 5555'),
    ('Juzgado 3ro', '333 Plaza de la Justicia, Villa Jurídica', '+444 555 6666'),
    ('Alcaldía de Panamá', '777 Calle Municipal, Pueblo Gubernamental', '+555 666 7777');
# Crear nuevo expediente
INSERT INTO Expedientes (IDExpediente, IDAseguradora, IDUsuario, FechaInicio, Descripcion)
VALUES
    (1, 1, 1, '2024-02-23', 'Nuevo expediente para Conductor');

# Crear número de caso y tipo de proceso
INSERT INTO Reportes (IDExpediente, FechaReporte, Descripcion)
VALUES
    (1, '2024-02-23', 'Conductor: Nombre del conductor, Aseguradora: Nombre de la aseguradora, Número de Caso: 12345, Tipo de Proceso: Judicial');
```

# Diagrama
# _____________________________________________________

<img width="888" alt="Screenshot 2024-02-22 at 8 55 55 PM" src="https://github.com/LightKnight23/BaseDeDatos2/assets/42986343/a0aa5963-a9a1-4ea6-a2b1-f17abdadbc7b">

