CREATE TABLE quotes (
   id serial PRIMARY KEY,
   name VARCHAR (50) NOT NULL,
   quote VARCHAR (512) NOT NULL
);

INSERT INTO quotes (name, quote) VALUES ('Q1', 'Q1Quote');
INSERT INTO quotes (name, quote) VALUES ('Q2', 'Q2Quote');
INSERT INTO quotes (name, quote) VALUES ('Q3', 'Q3Quote');