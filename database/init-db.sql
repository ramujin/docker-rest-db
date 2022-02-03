CREATE DATABASE IF NOT EXISTS ece140;

USE ece140;

-- DUMP EVERYTHING... YOU REALLY SHOULDN'T DO THIS!
DROP TABLE IF EXISTS Actors;

CREATE TABLE IF NOT EXISTS Actors (
  id          integer  AUTO_INCREMENT PRIMARY KEY,
  first_name  VARCHAR(30) NOT NULL,
  last_name   VARCHAR(30) NOT NULL,
  email       VARCHAR(50) NOT NULL,
  age         int,
  created_at  TIMESTAMP
);

INSERT INTO Actors (first_name, last_name, email, age, created_at) VALUES
  ("Zendaya", "", "zenny@greatestshowwoman.com", 25, CURRENT_TIMESTAMP),
  ("Tom", "Holland", "tom@ironmanrocks.com", 25, CURRENT_TIMESTAMP),
  ("Tobey", "Maguire", "tobey@originalspidey.com", 46, CURRENT_TIMESTAMP),
  ("Andrew", "Garfield", "andy@theamazingspidey.com", 38, CURRENT_TIMESTAMP)
;