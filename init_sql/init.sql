CREATE DATABASE myworkout;

USE myworkout;

CREATE TABLE IF NOT EXISTS myworkout_user (
	id INT NOT NULL AUTO_INCREMENT,
	nickname VARCHAR(32) NOT NULL,
	password_hash VARCHAR(128) NOT NULL,
	email VARCHAR(64) NOT NULL,
	timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS train(
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    description TEXT,
    myworkout_user_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
    FOREIGN KEY (myworkout_user_id) REFERENCES myworkout_user(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS exercise(
	id INT NOT NULL AUTO_INCREMENT,
myworkout_user_id INT NOT NULL,
    name VARCHAR(64) NOT NULL,
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
    FOREIGN KEY (myworkout_user_id) REFERENCES myworkout_user(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS muscle(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS exercise_muscle(
id INT NOT NULL AUTO_INCREMENT,
    exercise_id  INT NOT NULL,
    muscle_id INT NOT NULL,
    FOREIGN KEY (exercise_id) REFERENCES exercise(id)  ON DELETE CASCADE,
    FOREIGN KEY (muscle_id) REFERENCES muscle(id) ON DELETE CASCADE,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS train_exercise(
id INT NOT NULL AUTO_INCREMENT,
myworkout_user_id INT NOT NULL,
    sequence_number INT NOT NULL,
    train_id INT NOT NULL,
    exercise_id INT NOT NULL,
    reps INT NOT NULL,
    sets INT NOT NULL,
    timeout INT NOT NULL,
    FOREIGN KEY (exercise_id) REFERENCES exercise(id) ON DELETE CASCADE,
    FOREIGN KEY (train_id) REFERENCES train(id) ON DELETE CASCADE,
    FOREIGN KEY (myworkout_user_id) REFERENCES myworkout_user(id) ON DELETE CASCADE,
PRIMARY KEY (id)
);
