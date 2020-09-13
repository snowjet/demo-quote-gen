CREATE TABLE quotes (
   id serial PRIMARY KEY,
   name VARCHAR (50) NOT NULL,
   quote VARCHAR (512) NOT NULL
);

INSERT INTO quotes (name, quote) VALUES ('Steve Jobs', 'Real Artists Ship.');
INSERT INTO quotes (name, quote) VALUES ('Isaac Asimov', 'I do not fear computers. I fear lack of them.');
INSERT INTO quotes (name, quote) VALUES ('Bill Gates','The computer was born to solve problems that did not exist before.');
INSERT INTO quotes (name, quote) VALUES ('IBM Manual, 1925','All parts should go together without forcing.  You must remember that the parts you are reassembling were disassembled by you.  Therefore, if you can’t get them together again, there must be a reason.  By all means, do not use a hammer.');
INSERT INTO quotes (name, quote) VALUES ('Alan Bennett','Standards are always out of date.  That’s what makes them standards.');
INSERT INTO quotes (name, quote) VALUES ('Socrates','The more you know, the more you realize you know nothing.');
INSERT INTO quotes (name, quote) VALUES ('Benjamin Franklin','Tell me and I forget.  Teach me and I remember.  Involve me and I learn.');
INSERT INTO quotes (name, quote) VALUES ('Keith Bostic','Perl: The only language that looks the same before and after RSA encryption.');
INSERT INTO quotes (name, quote) VALUES ('Charles Simonyi','XML is not a language in the sense of a programming language any more than sketches on a napkin are a language.');