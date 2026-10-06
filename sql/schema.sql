CREATE DATABASE IF NOT EXISTS dormitory;

USE dormitory;

CREATE TABLE IF NOT EXISTS rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATETIME NOT NULL,
    sex CHAR(1) NOT NULL,
    room_id INT NOT NULL,

    CONSTRAINT fk_students_rooms
        FOREIGN KEY (room_id)
        REFERENCES rooms(id)
);