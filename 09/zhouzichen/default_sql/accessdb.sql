CREATE TABLE accessdb(user_id int NOT NULL auto_increment PRIMARY KEY, username varchar(30), password varchar(40), COMMENT varchar(10),UNIQUE (username))DEFAULT charset=utf8;