-- create schema dummy;
use club;

create table club_membership (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
	discription TEXT
);

CREATE TABLE club_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15),
    place VARCHAR(100),
    date DATE,
    dept VARCHAR(100),
    year VARCHAR(50),
    clubs TEXT,
    message TEXT
);
select * from club_members;


