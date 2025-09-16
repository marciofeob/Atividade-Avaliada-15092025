CREATE DATABASE atividade15092025;

USE atividade15092025;

CREATE TABLE usuarios (
    idusuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nivel_acesso ENUM('Administrador', 'Operador', 'Vendedor') NOT NULL
);

CREATE TABLE vendas (
    idvenda INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    usuario INT,
    FOREIGN KEY (usuario) REFERENCES usuarios(idusuario)
);

CREATE TABLE contasreceber (
    idcontasreceber INT AUTO_INCREMENT PRIMARY KEY,
    idvenda INT,
    datavencimento DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    usuario INT,
    FOREIGN KEY (usuario) REFERENCES usuarios(idusuario),
    FOREIGN KEY (idvenda) REFERENCES vendas(idvenda)
);




