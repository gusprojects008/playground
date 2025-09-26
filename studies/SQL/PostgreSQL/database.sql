-- TCL (Transaction Control Language)
BEGIN;

-- DDL (Data Definition Language)

DROP TABLE IF EXISTS Users, Stock;

CREATE TABLE IF NOT EXISTS Users (
  -- columnName datatype params
  resgistration_date DATE DEFAULT CURRENT_DATE,
  id SERIAL PRIMARY KEY, 
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL UNIQUE,
  active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Stock (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL (10,2) NOT NULL CHECK (price > 0)
);

-- TCL (Transaction Control Language)
COMMIT;
