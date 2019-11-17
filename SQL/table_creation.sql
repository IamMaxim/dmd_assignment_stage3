-- FOREIGN ​KEY​ (bug_id) REFERENCES Bugs(bug_id)

--SHOULD BE DEPENDANT FROM PATIENT
CREATE TABLE DIGITAL_MEDICAL_FILE (
    reg_number serial PRIMARY KEY,
    date_of_cretion datetime NOT NULL,
    patient_id int NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(id)
);

CREATE TABLE NUMBERS_OF_PREV_MEDICAL_FILES (
	id serial PRIMARY KEY,
	file_id REFERENCES DIGITAL_MEDICAL_FILE(reg_number),
	prev_file_id REFERENCES DIGITAL_MEDICAL_FILE(reg_number)
);


--SHOULD BE DEPENDANT FROM DIGITAL_MEDICAL_FILE
CREATE TABLE DIAGNOSE(
	name varchar(255) NOT NULL,
	di_id serial PRIMARY KEY,
	get_well_date datetime NOT NULL,
	found_date datetime NOT NULL,

	FOREIGN KEY () REFERENCES()
);

--SHOULD BE DEPENDANT FROM DIGITAL_MEDICAL_FILE
CREATE TABLE ANALYSE(
	res_id serial PRIMARY KEY, --to add to ERD
	collection_date datetime NOT NULL,
	results_avaliable boolean NOT NULL,
	results varchar(1023),
	FOREIGN KEY () REFERENCES()
);

CREATE TABLE PATIENT(
	age int NOT NULL,
	sex boolean NOT NULL, -- 0 is men, 1 woman
	id serial PRIMARY KEY,
	full_name varchar(255) NOT NULL

);

CREATE TABLE INVENTORY(
	item_id serial PRIMARY KEY,
	name varchar(255) NOT NULL,
	price_to_sell float(10,3), --can be null
	instruction varchar(1024) NOT NULL
);

CREATE TABLE SUPPLIERS(
	id serial PRIMARY​ KEY,
	inventory_id REFERENCES INVENTORY(item_id),
	supplier varchar(1024) NOT NULL,
	price_to_buy float(10,3) NOT NULL,
);

CREATE TABLE STAFF(
	st_id serial PRIMARY KEY,
	position varchar(255) NOT NULL
);

CREATE TABLE CHAT(
	name varchar(255) PRIMARY KEY,
);

CREATE TABLE MESSAGES(
	id serial PRIMARY​ KEY,
	messages varchar(1024)
	chat_id REFERENCES CHAT(name)
);

CREATE TABLE DOCTOR(
	working_hours varchar(255) NOT NULL,
	specialization varchar(255) NOT NULL,
	lisence_id serial PRIMARY KEY,
	name varchar(255) NOT NULL
);

CREATE TABLE AMBULANCE(
	assigned boolean NOT NULL,
	amd_id serial PRIMARY KEY,
	specialization varchar(255) NOT NULL,
	location varchar(255) NOT NULL
);

-- SHOUL BE DEPENDENT ON DOCTOR AND PATIENT
CREATE TABLE APPOINTMENT(
	ap_id serial PRIMARY KEY,
	date_and_time datetime NOT NULL,
	PRIMARY​ ​KEY​ ( ap_id, ),
	-- FOREIGN KEY () REFERENCES()
);

CREATE TABLE RECEPTIONIST(
	rec_id serial PRIMARY KEY,
	name varchar(255) NOT NULL,
	working_hours varchar(255) NOT NULL,
);

CREATE TABLE STAFF_INVENTORY(
	id serial PRIMARY KEY,
	staff_id REFERENCES STAFF(st_id),
	inventory_id REFERENCES INVENTORY(item_id)
);

CREATE TABLE PATIENT_INVENTORY(
	pat_inv_id serial PRIMARY KEY,
	patient_id REFERENCES PATIENT(id),
	inventory_id REFERENCES INVENTORY(item_id)
);

CREATE TABLE DOCTOR_INVENTORY(
	id serial PRIMARY KEY,
	doctor_id REFERENCES DOCTOR(lisence_id),
	inventory_id REFERENCES INVENTORY(item_id)
);

CREATE TABLE STAFF_CHAT(
	id serial PRIMARY KEY,
	chat_id REFERENCES CHAT(name),
	staff_id REFERENCES STAFF(st_id)
);

CREATE TABLE DOCTOR_CHAT(
	id serial PRIMARY KEY,
	chat_id REFERENCES CHAT(name),
	doctor_id REFERENCES DOCTOR(lisence_id),
);

CREATE TABLE CHAT_RECEPTIONIST(
	id serial PRIMARY KEY,
	chat_id REFERENCES CHAT(name),
	receptionist_id REFERENCES RECEPTIONIST(rec_id),
);

CREATE TABLE RECEPTIONIST_AMBULANCE(
	id serial PRIMARY KEY,
	ambulance_id REFERENCES AMBULANCE(amd_id),
	receptionist_id REFERENCES RECEPTIONIST(rec_id)
);

CREATE TABLE RECEPTIONIST_PATIENT(
	id serial PRIMARY KEY,
	patient_id REFERENCES PATIENT(id),
	receptionist_id REFERENCES RECEPTIONIST(rec_id)
);










