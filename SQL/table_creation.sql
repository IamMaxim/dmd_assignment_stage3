CREATE TABLE PATIENT(
	age int NOT NULL,
	sex boolean NOT NULL, -- 0 is men, 1 woman
	id serial PRIMARY KEY,
	full_name varchar(255) NOT NULL
);

CREATE TABLE DIGITAL_MEDICAL_FILE (
    reg_number serial UNIQUE NOT NULL,
    date_of_cretion timestamp NOT NULL,
    patient_id int NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(id),
    PRIMARY KEY (reg_number, patient_id)
);

CREATE TABLE NUMBERS_OF_PREV_MEDICAL_FILES (
	id serial PRIMARY KEY,
	file_id int  REFERENCES DIGITAL_MEDICAL_FILE(reg_number),
	prev_file_id int REFERENCES DIGITAL_MEDICAL_FILE(reg_number)
);


CREATE TABLE DIAGNOSE(
	name varchar(255) NOT NULL,
	di_id serial UNIQUE NOT NULL,
	get_well_date timestamp NOT NULL,
	found_date timestamp NOT NULL,
	reg_number int NOT NULL,
	patient_id int NOT NULL,
	treatment varchar(1023) NOT NULL, --add to erd
	FOREIGN KEY (reg_number, patient_id)
	REFERENCES DIGITAL_MEDICAL_FILE(reg_number, patient_id),
	PRIMARY KEY (reg_number, patient_id, di_id)
);

CREATE TABLE MED_TEST(
	res_id serial UNIQUE NOT NULL , --to add to ERD
	collection_date timestamp NOT NULL,
	results_avaliable boolean NOT NULL,
	results varchar(1023),
	reg_number int NOT NULL,
	patient_id int NOT NULL,
	FOREIGN KEY (reg_number, patient_id)
	REFERENCES DIGITAL_MEDICAL_FILE(reg_number, patient_id),
	PRIMARY KEY (reg_number, patient_id, res_id)
);

CREATE TABLE INVENTORY(
	item_id serial PRIMARY KEY,
	name varchar(255) NOT NULL,
	price_to_sell decimal, --can be null
	instruction varchar(1024) NOT NULL
);


CREATE TABLE SUPPLIERS(
	id serial UNIQUE NOT NULL ,
	item_id int NOT NULL ,
	supplier varchar(1024) NOT NULL,
	price_to_buy decimal NOT NULL,
	FOREIGN KEY (item_id)
	REFERENCES INVENTORY(item_id),
	PRIMARY KEY (item_id, id)
);

CREATE TABLE STAFF(
	st_id serial PRIMARY KEY,
	position varchar(255) NOT NULL
);

CREATE TABLE CHAT(
	name varchar(255) PRIMARY KEY
);

CREATE TABLE MESSAGES(
	id serial UNIQUE NOT NULL ,
	messages varchar(1024),
	name varchar(255) NOT NULL,
	FOREIGN KEY (name)
	REFERENCES CHAT(name),
	PRIMARY KEY (id, name)
);

CREATE TABLE DOCTOR(
	working_hours varchar(255) NOT NULL,
	specialization varchar(255) NOT NULL,
	name varchar(255) NOT NULL,
	lisence_id serial PRIMARY KEY
);

CREATE TABLE AMBULANCE(
	assigned boolean NOT NULL,
	amd_id serial PRIMARY KEY,
	specialization varchar(255) NOT NULL,
	location varchar(255) NOT NULL
);

CREATE TABLE RECEPTIONIST(
	rec_id serial PRIMARY KEY,
	name varchar(255) NOT NULL,
	working_hours varchar(255) NOT NULL
);

CREATE TABLE APPOINTMENT(
	patient_id int NOT NULL,
	rec_id int NOT NULL,
	doctor_id int NOT NULL,
	ap_id serial UNIQUE,
	date_and_time timestamp NOT NULL,
	FOREIGN KEY (patient_id) REFERENCES PATIENT(id),
	FOREIGN KEY (doctor_id) REFERENCES DOCTOR(lisence_id),
	FOREIGN KEY(rec_id) REFERENCES RECEPTIONIST(rec_id),
	PRIMARY KEY (ap_id, patient_id, doctor_id, rec_id)
);

CREATE TABLE STAFF_INVENTORY(
	id serial,
	staff_id int NOT NULL,
	FOREIGN KEY (staff_id)
	REFERENCES STAFF(st_id),
	inventory_id int NOT NULL ,
	FOREIGN KEY (inventory_id)
	REFERENCES INVENTORY(item_id),
	PRIMARY KEY (id, inventory_id)
);

CREATE TABLE PATIENT_INVENTORY(
	pat_inv_id serial UNIQUE NOT NULL,
	patient_id int NOT NULL,
	FOREIGN KEY (patient_id)
	REFERENCES PATIENT(id),
	inventory_id int not null,
	FOREIGN KEY (inventory_id)
	REFERENCES INVENTORY(item_id),
	PRIMARY KEY(pat_inv_id, patient_id, inventory_id)
);

CREATE TABLE DOCTOR_INVENTORY(
	id serial UNIQUE NOT NULL,
	doctor_id int not null,
	FOREIGN KEY (doctor_id)
	REFERENCES DOCTOR(lisence_id),
	inventory_id int not null,
	FOREIGN KEY (inventory_id)
	REFERENCES INVENTORY(item_id),
	PRIMARY KEY (inventory_id, doctor_id, id)
);

CREATE TABLE STAFF_CHAT(
	id serial UNIQUE NOT NULL,
	chat_id varchar(255) NOT NULL,
	FOREIGN KEY (chat_id)
	REFERENCES CHAT(name),
	staff_id int NOT NULL,
	FOREIGN KEY (staff_id)
	REFERENCES STAFF(st_id),
	PRIMARY KEY(id, chat_id,staff_id)
);

CREATE TABLE DOCTOR_CHAT(
	id serial UNIQUE NOT NULL ,
	chat_id varchar(255) NOT NULL,
	FOREIGN KEY (chat_id)
	REFERENCES CHAT(name),
	doctor_id int not null,
	FOREIGN KEY (doctor_id)
	REFERENCES DOCTOR(lisence_id),
	PRIMARY KEY (doctor_id,chat_id, id)
);

CREATE TABLE CHAT_RECEPTIONIST(
	id serial UNIQUE NOT NULL,
	chat_id  varchar(255) NOT NULL,
	FOREIGN KEY (chat_id)
	REFERENCES CHAT(name),
	receptionist_id int NOT NULL,
	FOREIGN KEY (receptionist_id)
	REFERENCES RECEPTIONIST(rec_id),
	PRIMARY KEY(id, chat_id, receptionist_id)
);

CREATE TABLE RECEPTIONIST_AMBULANCE(
	id serial UNIQUE NOT NULL,
	ambulance_id int NOT NULL ,
	FOREIGN KEY (ambulance_id)
	REFERENCES AMBULANCE(amd_id),
	receptionist_id int NOT NULL,
	FOREIGN KEY (receptionist_id)
	REFERENCES RECEPTIONIST(rec_id),
	PRIMARY KEY(id, receptionist_id,ambulance_id)
);

CREATE TABLE RECEPTIONIST_PATIENT(
	id serial UNIQUE NOT NULL,
	patient_id int not NULL,
	FOREIGN KEY (patient_id)
	REFERENCES PATIENT(id),
	receptionist_id int NOT NULL,
	FOREIGN KEY (receptionist_id)
	REFERENCES RECEPTIONIST(rec_id),
	PRIMARY KEY (id, patient_id, receptionist_id)
);