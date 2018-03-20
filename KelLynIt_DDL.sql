CREATE TABLE Business (
	business_id	CHAR(22) PRIMARY KEY,
	name VARCHAR(75) NOT NULL,
	address VARCHAR(100) NOT NULL,
	city VARCHAR(20) NOT NULL,
	state_code CHAR(2) NOT NULL,
	postal_code CHAR(5) NOT NULL,
	latitude FLOAT NOT NULL,
	longitude FLOAT NOT NULL,
	stars FLOAT CHECK (stars <= 5 AND stars >= 0) NOT NULL,
	reviewcount INTEGER NOT NULL,
	is_open INTEGER CHECK (is_open = 0 OR is_open = 1) NOT NULL,
	numCheckins INTEGER NOT NULL,
	reviewrating FLOAT NOT NULL);
	
CREATE TABLE HOURS (
	dayOfWeek	VARCHAR(10),
	open		TIME,
	close		TIME,
	business_id	CHAR(22),
	PRIMARY KEY (dayOfWeek, business_id),
	FOREIGN KEY (business_id) REFERENCES Business (business_id));

CREATE TABLE CATEGORIES (
	category_name	VARCHAR(50),
	business_id		VARCHAR(22),
	PRIMARY KEY (category_name, business_id),
	FOREIGN KEY (business_id) REFERENCES Business (business_id));
	
CREATE TABLE Users (
	user_id			CHAR(22) PRIMARY KEY,
	yelping_since	DATE NOT NULL,
	name			VARCHAR(50) NOT NULL,
	review_count	INTEGER,
	useful			INTEGER,
	funny			INTEGER,
	fans			INTEGER,
	cool			INTEGER,
	average_stars	FLOAT CHECK (average_stars <= 5.0 AND average_stars >= 0.0));
	
CREATE TABLE Checkins (
	day				VARCHAR(10),
	start_time		VARCHAR(15),
	num_checkins	INTEGER,
	business_id		VARCHAR(22),
	PRIMARY KEY (day, start_time, business_id),
	FOREIGN KEY (business_id) REFERENCES Business (business_id));
	
CREATE TABLE Review (
	review_id		CHAR(22) PRIMARY KEY,
	user_id			CHAR(22) NOT NULL,
	business_id		CHAR(22) NOT NULL,
	date			DATE NOT NULL,
	text			VARCHAR(5000) NOT NULL,
	stars			FLOAT CHECK (stars <= 5.0 AND stars >= 0.0) NOT NULL,
	funny			INTEGER,
	cool			INTEGER,
	useful			INTEGER,
	FOREIGN KEY (user_id) REFERENCES Users (user_id),
	FOREIGN KEY (business_id) REFERENCES Business (business_id)
);

CREATE TABLE Friends (
	user_id			CHAR(22),
	friend_id		CHAR(22),
	PRIMARY KEY (user_id, friend_id),
	FOREIGN KEY (user_id) REFERENCES Users (user_id),
    FOREIGN KEY (friend_id) REFERENCES Users (user_id)
);