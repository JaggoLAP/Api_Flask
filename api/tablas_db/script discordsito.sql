CREATE DATABASE devpro;
USE devpro;
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nac VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    imagen_perfil VARCHAR(255) DEFAULT 'default.jpg',
    estado VARCHAR(10) NOT NULL
);
CREATE TABLE servidores (
    id_servidor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servidor VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    fecha_creacion_servidor TIMESTAMP,
    imagen_servidor VARCHAR (255),
    id_creador_servidor INT NOT NULL
);
CREATE TABLE miembro_servidor (
    id_miembro INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    servidor_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (servidor_id) REFERENCES servidores(id_servidor)
);
CREATE TABLE canales (
    id_canal INT AUTO_INCREMENT PRIMARY KEY,
    nombre_canal VARCHAR(255) NOT NULL,
    servidor_id INT,
    fecha_creacion_canal TIMESTAMP,
    id_creador_canal INT NOT NULL,
    FOREIGN KEY (servidor_id) REFERENCES servidores(id_servidor)
);
CREATE TABLE mensajes (
    id_mensaje INT AUTO_INCREMENT PRIMARY KEY,
    contenido TEXT NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT,
    canal_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (canal_id) REFERENCES canales(id_canal)
);
