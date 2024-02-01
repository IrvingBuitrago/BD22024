CREATE DATABASE db2_2024;

USE db2_2024;

CREATE TABLE entidades (
    id_entidad INT PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100),
    telefono INT,
    id_cliente INT,
    id_bita INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_bita) REFERENCES bitacoras(id_bita));

CREATE TABLE roles (
    id_rol INT PRIMARY KEY NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    PERMISOS VARCHAR(100),
    id_cliente INT,
    id_bita INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_bita) REFERENCES bitacoras(id_bita));

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono INT NOT NULL,
    id_rol INT,
    id_entidad INT,
    id_bita INT,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    FOREIGN KEY (id_entidad) REFERENCES entidades(id_entidad),
    FOREIGN KEY (id_bita) REFERENCES bitacoras(id_bita));

CREATE TABLE transacciones (
    id_tran INT PRIMARY KEY NOT NULL,
    monto INT NOT NULL,
    fecha DATETIME NOT NULL,
    id_cliente INT,
    id_entidad INT,
    id_bita INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_entidad) REFERENCES entidades(id_entidad),
    FOREIGN KEY (id_bita) REFERENCES bitacoras(id_bita));

CREATE TABLE bitacoras (
    id_bit INT PRIMARY KEY NOT NULL,
    fecha DATETIME NOT NULL,
    descripcion VARCHAR(128),
    id_cliente INT,
    id_entidad INT,
    id_tran INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_entidad) REFERENCES entidades(id_entidad),
    FOREIGN KEY (id_tran) REFERENCES transacciones(id_tran));

INSERT INTO entidades VALUES(1, "uber"), (2, "indrive"), (3, "pedidosya");
INSERT INTO clientes VALUES(86547125, "Federico", "Valverde", 64743458)

SELECT * FROM entidades
WHERE nombre = "uber";

UPDATE clientes SET telefono = 69758321
WHERE id_cliente = 86547125;

DELETE FROM entidades
WHERE id_entidad = 1;



