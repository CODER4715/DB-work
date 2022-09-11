DROP DATABASE IF EXISTS Flight_Sys;
CREATE DATABASE IF NOT EXISTS Flight_Sys
DEFAULT CHARACTER SET utf8mb4	
DEFAULT COLLATE utf8mb4_unicode_ci;

Use Flight_Sys;

#航空公司表
CREATE TABLE IF NOT EXISTS airline(
code	char(3)	PRIMARY KEY,
airlinename	varchar(1024) 	not null
);

#机场表
CREATE TABLE IF NOT EXISTS airport(
airportno	char(4)	PRIMARY KEY,
airportname varchar(100)	not null
);

#航班表
CREATE TABLE IF NOT EXISTS flight(
flightno	char(7)	PRIMARY KEY,
dept_airport	char(4)	not null,
arv_airport	char(4)	not null,
code		char(3)	not null,
FOREIGN KEY (dept_airport) REFERENCES airport (airportno)
	ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (arv_airport) REFERENCES airport (airportno)
	ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (code) REFERENCES airline (code)
	ON DELETE CASCADE ON UPDATE CASCADE
);

#班次表(加过座位等级)
CREATE TABLE IF NOT EXISTS timetable(
flightno	char(7),
deptdate	int(8),
depttime	smallint(4)	not null,
arvtime char(5)	not null,
flight_status varchar(4) not null,
seats_eco	smallint(4)	not null,
seats_lux	smallint(4) not null,
seats_ceco	smallint(4)	not null,
seats_clux	smallint(4) not null,
FOREIGN KEY (flightno) REFERENCES flight (flightno)
	ON DELETE CASCADE ON UPDATE CASCADE,
PRIMARY KEY(deptdate,flightno)
);

#票价表
CREATE TABLE IF NOT EXISTS price(
	flightno char(7),
	deptdate int(8),
	eco_price FLOAT,
	lux_price FLOAT,
	FOREIGN KEY (deptdate,flightno) REFERENCES timetable(deptdate,flightno)
	ON DELETE CASCADE ON UPDATE CASCADE
);

#乘客表
CREATE TABLE IF NOT EXISTS passenger(
id_passportno varchar(50) PRIMARY KEY,
nationality	varchar(20),
tel	bigint(11)	,
enname	varchar(50)
);

#中国人表
CREATE TABLE IF NOT EXISTS chinese(
id_passportno varchar(50) PRIMARY KEY,
cnname	varchar(20),
ethnic	char(5),
sex varchar(2),
FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
	ON DELETE CASCADE ON UPDATE CASCADE
);

#外国人表
CREATE TABLE IF NOT EXISTS foreigner(
id_passportno varchar(50) PRIMARY KEY,
visano	varchar(100),
sex varchar(8),
FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
	ON DELETE CASCADE ON UPDATE CASCADE
);

#购票表
CREATE TABLE IF NOT EXISTS ticket(
flightno	char(7),
deptdate	int(8),
seat	smallint(4)	not null,
seat_class	smallint(1) not null,
id_passportno	varchar(50)	not null,
PRIMARY KEY (flightno,deptdate,seat,seat_class)
);

ALTER TABLE `ticket`
	ADD FOREIGN KEY (deptdate) REFERENCES timetable (deptdate)
		ON DELETE CASCADE ON UPDATE CASCADE,
	ADD FOREIGN KEY (flightno) REFERENCES timetable (flightno)
		ON DELETE CASCADE ON UPDATE CASCADE,
	ADD FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
		ON DELETE NO ACTION ON UPDATE CASCADE;
