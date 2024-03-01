Parcial 1 Base de Datos II

Nombres: Eyvar García, Efraín Fox


Problema 1
```sql
-- Creación de la base de datos
CREATE SCHEMA Pentesting;

-- Selección de la base de datos
USE Pentesting;

-- Creación de la tabla para el módulo de tipos de pruebas
CREATE TABLE TiposPruebas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    referencia VARCHAR(255) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_ingreso DATE,
    estado VARCHAR(10)
);

-- Creación de la tabla para el módulo de usuarios
CREATE TABLE Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    nombre_usuario VARCHAR(255) NOT NULL UNIQUE,
    token VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    ciudad VARCHAR(255),
    sexo VARCHAR(10),
    estado_civil VARCHAR(20),
    tipo_empresa VARCHAR(20),
    direccion VARCHAR(255),
    tipo_prueba_id INT,
    FOREIGN KEY (tipo_prueba_id) REFERENCES TiposPruebas(id)
);

-- Creación de la tabla para el módulo de autenticación
CREATE TABLE Autenticacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    agente_usuario VARCHAR(255),
    token VARCHAR(255) NOT NULL UNIQUE,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);


-- Creación de la tabla para el módulo de pago
CREATE TABLE Pagos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_compania VARCHAR(255) NOT NULL,
    nombre_cliente VARCHAR(255) NOT NULL,
    apellido_cliente VARCHAR(255) NOT NULL,
    numero_vat VARCHAR(20) NOT NULL,
    direccion_pago VARCHAR(255),
    ciudad_pago VARCHAR(255),
    codigo_postal_pago VARCHAR(20),
    pais_pago VARCHAR(255),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);

-- Inserción de 10 registros en cada tabla (ejemplo)
-- Módulo de autenticación
INSERT INTO Autenticacion (nombre_usuario, contrasena, agente_usuario, token)
VALUES
('user1', 'pass123', 'Laptop1', 'token_user1'),
('user2', 'pass456', 'Mobile2', 'token_user2'),
('user3', 'pass789', 'Desktop3', 'token_user3'),
('user4', 'passabc', 'Tablet4', 'token_user4'),
('user5', 'passxyz', 'Mobile5', 'token_user5'),
('user6', 'pass456', 'Laptop6', 'token_user6'),
('user7', 'passabc', 'Desktop7', 'token_user7'),
('user8', 'pass123', 'Mobile8', 'token_user8'),
('user9', 'pass789', 'Laptop9', 'token_user9'),
('user10', 'passxyz', 'Tablet10', 'token_user10');


-- Módulo de usuarios
INSERT INTO Usuarios (nombre, apellido, nombre_usuario, token, contrasena, ciudad, sexo, estado_civil, tipo_empresa, direccion)
VALUES
('Alice', 'Johnson', 'alice_j', 'token_user3', 'pass789', 'New York', 'Female', 'Married', 'Privada', '123 Main St'),
('Bob', 'Williams', 'bob_w', 'token_user4', 'passabc', 'Los Angeles', 'Male', 'Single', 'Publica', '456 Oak St'),
('Charlie', 'Brown', 'charlie_b', 'token_user5', 'passxyz', 'London', 'Male', 'Single', 'Privada', '789 Pine St'),
('David', 'Miller', 'david_m', 'token_user6', 'pass456', 'Paris', 'Male', 'Married', 'Publica', '101 Elm St'),
('Eva', 'Davis', 'eva_d', 'token_user7', 'passabc', 'Sydney', 'Female', 'Single', 'Privada', '202 Cedar St'),
('Frank', 'Johnson', 'frank_j', 'token_user8', 'pass123', 'Toronto', 'Male', 'Married', 'Publica', '303 Maple St'),
('Grace', 'Taylor', 'grace_t', 'token_user9', 'pass789', 'Berlin', 'Female', 'Single', 'Privada', '404 Birch St'),
('Henry', 'Smith', 'henry_s', 'token_user10', 'passxyz', 'Tokyo', 'Male', 'Married', 'Publica', '505 Walnut St'),
('Ivy', 'Martin', 'ivy_m', 'token_user11', 'pass123', 'Mumbai', 'Female', 'Single', 'Privada', '606 Pine St'),
('Jack', 'White', 'jack_w', 'token_user12', 'passabc', 'Beijing', 'Male', 'Married', 'Publica', '707 Oak St');

-- Módulo de tipos de pruebas
INSERT INTO TiposPruebas (referencia, nombre, descripcion, fecha_ingreso, estado)
VALUES
('REF1', 'Penetración de Red', 'Prueba de seguridad en red', '2024-02-29', 'Activo'),
('REF2', 'Aplicaciones Web', 'Prueba de seguridad web', '2024-02-29', 'Activo'),
('REF3', 'Aplicaciones Móviles', 'Prueba de seguridad móvil', '2024-02-29', 'Activo'),
('REF4', 'Sistemas Operativos', 'Prueba de seguridad de sistemas operativos', '2024-02-29', 'Activo'),
('REF5', 'Wi-Fi', 'Prueba de seguridad Wi-Fi', '2024-02-29', 'Activo'),
('REF6', 'Seguridad Física', 'Prueba de seguridad física', '2024-02-29', 'Activo'),
('REF7', 'Ingeniería Social', 'Prueba de ingeniería social', '2024-02-29', 'Activo'),
('REF8', 'Seguridad en la Nube', 'Prueba de seguridad en la nube', '2024-02-29', 'Activo'),
('REF9', 'Seguridad de Hardware', 'Prueba de seguridad de hardware', '2024-02-29', 'Activo'),
('REF10', 'Análisis de Código Fuente', 'Prueba de análisis de código fuente', '2024-02-29', 'Activo');

-- Módulo de pago
INSERT INTO Pagos (nombre_compania, nombre_cliente, apellido_cliente, numero_vat, direccion_pago, ciudad_pago, codigo_postal_pago, pais_pago)
VALUES
('Company1', 'Alice', 'Johnson', 'VAT123', 'PaymentAddress1', 'New York', '12345', 'United States'),
('Company2', 'Bob', 'Williams', 'VAT456', 'PaymentAddress2', 'Los Angeles', '67890', 'United States'),
('Company3', 'Charlie', 'Brown', 'VAT789', 'PaymentAddress3', 'London', '23456', 'United Kingdom'),
('Company4', 'David', 'Miller', 'VAT012', 'PaymentAddress4', 'Paris', '78901', 'France'),
('Company5', 'Eva', 'Davis', 'VAT345', 'PaymentAddress5', 'Sydney', '34567', 'Australia'),
('Company6', 'Frank', 'Johnson', 'VAT678', 'PaymentAddress6', 'Toronto', '89012', 'Canada'),
('Company7', 'Grace', 'Taylor', 'VAT901', 'PaymentAddress7', 'Berlin', '45678', 'Germany'),
('Company8', 'Henry', 'Smith', 'VAT234', 'PaymentAddress8', 'Tokyo', '01234', 'Japan'),
('Company9', 'Ivy', 'Martin', 'VAT567', 'PaymentAddress9', 'Mumbai', '56789', 'India'),
('Company10', 'Jack', 'White', 'VAT890', 'PaymentAddress10', 'Beijing', '98765', 'China');
```

Diagrama Entidad-Relación

 <img width="468" alt="image" src="https://github.com/LightKnight23/BaseDeDatos2/assets/42986343/33a92b35-db9c-458e-ae34-64755e76d645">

Problema 2
```sql
-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS DiseñoModa;
USE DiseñoModa;

-- Creación de las tablas mediante el lenguaje DDL
CREATE TABLE tamano (
    tamano_id INT PRIMARY KEY,
    codigo_tamano VARCHAR(255) NOT NULL,
    clasificacion VARCHAR(255) NOT NULL,
    alto DECIMAL NOT NULL, -- Nuevo campo
    ancho DECIMAL NOT NULL, -- Nuevo campo
    estado_de_la_ropa ENUM('Nuevo', 'Usado')
);

CREATE TABLE categoria (
    categoria_id INT PRIMARY KEY,
    categoria_principal VARCHAR(255) NOT NULL,
    material VARCHAR(255), -- Nuevo campo
    estado ENUM('Nuevo', 'Usado'), -- Nuevo campo
	categoria_edad ENUM('Niños', 'Adultos'), -- Nuevo campo
    categorias_sexo ENUM('Hombres', 'Mujeres') -- Nuevo campo
);

CREATE TABLE color (
    color_id INT PRIMARY KEY,
    codigo_color VARCHAR(255) NOT NULL,
    nombre_color VARCHAR(255) NOT NULL,
    hexadecimal VARCHAR(7), -- Nuevo campo
    disponible BOOLEAN -- Nuevo campo
);


CREATE TABLE producto (
    producto_id INT PRIMARY KEY,
    nombre_producto VARCHAR(255) NOT NULL,
    cantidad INT, -- Nuevo campo
    disponibilidad BOOLEAN, -- Nuevo campo
    tamano_id INT,
    categoria_id INT,
    color_id INT,
    FOREIGN KEY (tamano_id) REFERENCES tamano(tamano_id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(categoria_id),
    FOREIGN KEY (color_id) REFERENCES color(color_id)
);
CREATE TABLE colores_producto (
    color_id INT,
    producto_id INT, -- Nuevo campo
    cantidad_diposible INT,  -- Nuevo campo
    PRIMARY KEY (color_id, producto_id),
    FOREIGN KEY (color_id) REFERENCES color(color_id),
    FOREIGN KEY (producto_id) REFERENCES producto(producto_id)
);


CREATE TABLE categorias_producto (
    categoria_id INT,
    producto_id INT, -- nuevo campo
    decripcion VARCHAR(500), -- nuevo campo
    PRIMARY KEY (categoria_id, producto_id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(categoria_id),
    FOREIGN KEY (producto_id) REFERENCES producto(producto_id)
);

-- Inserción de datos en lenguaje DML

-- Inserción de datos en la tabla 'tamano'
INSERT IGNORE INTO tamano (tamano_id, codigo_tamano, clasificacion, alto, ancho, estado_de_la_ropa)
VALUES
(1, 'T001', 'Pequeño', 20.5, 15.2, 'Nuevo'),
(2, 'T002', 'Mediano', 30.0, 25.0, 'Nuevo'),
(3, 'T003', 'Grande', 40.0, 35.5, 'Usado'),
(4, 'T004', 'Pequeño', 18.0, 12.5, 'Nuevo'),
(5, 'T005', 'Grande', 35.0, 28.0, 'Nuevo'),
(6, 'T006', 'Mediano', 25.0, 20.0, 'Usado'),
(7, 'T007', 'Grande', 38.0, 30.0, 'Nuevo'),
(8, 'T008', 'Pequeño', 16.5, 10.0, 'Usado'),
(9, 'T009', 'Mediano', 28.0, 22.5, 'Nuevo'),
(10, 'T010', 'Grande', 42.0, 34.0, 'Nuevo');


-- Inserción de datos en la tabla 'categoria'
INSERT INTO categoria (categoria_id, categoria_principal, material, estado, categoria_edad, categorias_sexo)
VALUES
(1, 'Ropa deportiva', 'Algodón', 'Nuevo', 'Adultos', 'Mujeres'),
(2, 'Calzado casual', 'Cuero', 'Nuevo', 'Adultos', 'Hombres'),
(3, 'Ropa infantil', 'Poliéster', 'Nuevo', 'Niños', 'Mujeres'),
(4, 'Ropa casual', 'Denim', 'Nuevo', 'Adultos', 'Hombres'),
(5, 'Ropa formal', 'Seda', 'Nuevo', 'Adultos', 'Mujeres'),
(6, 'Ropa deportiva', 'Licra', 'Usado', 'Adultos', 'Mujeres'),
(7, 'Calzado deportivo', 'Sintético', 'Nuevo', 'Niños', 'Hombres'),
(8, 'Ropa formal', 'Algodón', 'Nuevo', 'Adultos', 'Mujeres'),
(9, 'Accesorios', 'Piel', 'Nuevo', 'Adultos', 'Mujeres'),
(10, 'Ropa casual', 'Denim', 'Nuevo', 'Adultos', 'Hombres');

-- Inserción de datos en la tabla 'color'
INSERT INTO color (color_id, codigo_color, nombre_color, hexadecimal, disponible)
VALUES
(1, 'C001', 'Rojo', '#FF0000', TRUE),
(2, 'C002', 'Azul', '#0000FF', TRUE),
(3, 'C003', 'Verde', '#00FF00', TRUE),
(4, 'C004', 'Amarillo', '#FFFF00', TRUE),
(5, 'C005', 'Negro', '#000000', TRUE),
(6, 'C006', 'Blanco', '#FFFFFF', TRUE),
(7, 'C007', 'Gris', '#808080', TRUE),
(8, 'C008', 'Morado', '#800080', TRUE),
(9, 'C009', 'Naranja', '#FFA500', TRUE),
(10, 'C010', 'Rosa', '#FFC0CB', TRUE);

-- Inserción de datos en la tabla 'colores_producto'
INSERT INTO colores_producto (color_id, producto_id, cantidad_diposible)
VALUES
(1, 1, 50),
(2, 1, 30),
(3, 2, 20),
(4, 1, 10),
(5, 2, 15),
(4, 3, 25),
(6, 2, 10),
(7, 3, 20),
(8, 4, 30),
(9, 5, 15),
(10, 1, 25);

-- Inserción de datos en la tabla 'producto'
INSERT INTO producto (producto_id, nombre_producto, cantidad, disponibilidad, tamano_id, categoria_id, color_id)
VALUES
(1, 'Camiseta deportiva', 100, TRUE, 1, 1, 1),
(2, 'Zapatos casuales', 50, TRUE, 2, 2, 2),
(3, 'Vestido infantil', 80, TRUE, 3, 3, 3),
(4, 'Jeans ajustados', 70, TRUE, 4, 4, 5),
(5, 'Vestido de noche', 40, TRUE, 5, 5, 2),
(6, 'Chaqueta deportiva', 60, TRUE, 6, 6, 6),
(7, 'Zapatillas deportivas', 35, TRUE, 7, 7, 7),
(8, 'Traje formal', 20, TRUE, 8, 8, 8),
(9, 'Bolso de mano', 45, TRUE, 9, 9, 9),
(10, 'Camisa casual', 55, TRUE, 10, 10, 10);

-- Inserción de datos en la tabla 'categorias_del_producto'
INSERT INTO categorias_producto (categoria_id, producto_id, decripcion)
VALUES
(1, 1, 'Camisetas deportivas para mujeres adultas'),
(2, 2, 'Zapatos casuales para hombres adultos'),
(3, 3, 'Vestidos infantiles para niñas'),
(4, 4, 'Jeans casuales para hombres'),
(5, 5, 'Vestido formal para mujeres'),
(6, 6, 'Chaqueta deportiva para mujeres'),
(7, 7, 'Zapatillas deportivas para niños'),
(8, 8, 'Traje formal para mujeres'),
(9, 9, 'Bolso de mano unisex'),
(10, 10, 'Camisa casual para hombres');
```
 

<img width="442" alt="image" src="https://github.com/LightKnight23/BaseDeDatos2/assets/42986343/1cc370f1-7c7d-4bd2-85ae-b57808e1f1b2">

