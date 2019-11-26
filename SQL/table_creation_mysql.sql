# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;

CREATE TABLE if not exists PATIENT
(
    age       int          NOT NULL,
    sex       boolean      NOT NULL, -- 0 is men, 1 woman
    id        serial PRIMARY KEY,
    full_name varchar(255) NOT NULL
);

CREATE TABLE if not exists DIGITAL_MEDICAL_FILE
(
    reg_number       serial UNIQUE       NOT NULL,
    date_of_creation timestamp           NOT NULL,
    patient_id       bigint(20) unsigned NOT NULL,
    FOREIGN KEY (patient_id)
        REFERENCES PATIENT (id)
        ON DELETE CASCADE,
    PRIMARY KEY (reg_number, patient_id)
);

CREATE TABLE if not exists NUMBERS_OF_PREV_MEDICAL_FILES
(
    id           serial PRIMARY KEY,
    file_id      bigint(20) unsigned REFERENCES DIGITAL_MEDICAL_FILE (reg_number),
    prev_file_id bigint(20) unsigned REFERENCES DIGITAL_MEDICAL_FILE (reg_number)
);


CREATE TABLE if not exists DIAGNOSE
(
    name          varchar(255)        NOT NULL,
    di_id         serial UNIQUE       NOT NULL,
    get_well_date timestamp           NOT NULL,
    found_date    timestamp           NOT NULL,
    reg_number    bigint(20) unsigned NOT NULL,
    patient_id    bigint(20) unsigned NOT NULL,
    treatment     varchar(1023)       NOT NULL,
    FOREIGN KEY (reg_number, patient_id)
        REFERENCES DIGITAL_MEDICAL_FILE (reg_number, patient_id)
        ON DELETE CASCADE,
    PRIMARY KEY (reg_number, patient_id, di_id)
);

CREATE TABLE if not exists MED_TEST
(
    res_id            serial UNIQUE       NOT NULL,
    collection_date   timestamp           NOT NULL,
    results_available boolean             NOT NULL,
    results           varchar(1023),
    reg_number        bigint(20) unsigned NOT NULL,
    patient_id        bigint(20) unsigned NOT NULL,
    FOREIGN KEY (reg_number, patient_id)
        REFERENCES DIGITAL_MEDICAL_FILE (reg_number, patient_id)
        ON DELETE CASCADE,
    PRIMARY KEY (reg_number, patient_id, res_id)
);

CREATE TABLE if not exists INVENTORY
(
    item_id       serial PRIMARY KEY,
    name          varchar(255)  NOT NULL,
    price_to_sell decimal,
    instruction   varchar(1024) NOT NULL
);


CREATE TABLE if not exists SUPPLIERS
(
    id           serial UNIQUE       NOT NULL,
    item_id      bigint(20) unsigned NOT NULL,
    supplier     varchar(1024)       NOT NULL,
    price_to_buy decimal             NOT NULL,
    FOREIGN KEY (item_id)
        REFERENCES INVENTORY (item_id)
        ON DELETE CASCADE,
    PRIMARY KEY (item_id, id)
);

CREATE TABLE if not exists STAFF
(
    st_id    serial PRIMARY KEY,
    position varchar(255) NOT NULL
);

CREATE TABLE if not exists CHAT
(
    name varchar(255) PRIMARY KEY
);

CREATE TABLE if not exists MESSAGES
(
    id       serial UNIQUE NOT NULL,
    messages varchar(1024),
    name     varchar(255)  NOT NULL,
    FOREIGN KEY (name)
        REFERENCES CHAT (name)
        ON DELETE CASCADE,
    PRIMARY KEY (id, name)
);

CREATE TABLE if not exists DOCTOR
(
    id             serial primary key,
    working_hours  varchar(255) NOT NULL,
    specialization varchar(255) NOT NULL,
    name           varchar(255) NOT NULL,
    license_id     bigint(20) unsigned
);

CREATE TABLE if not exists AMBULANCE
(
    assigned       boolean      NOT NULL,
    amd_id         serial PRIMARY KEY,
    specialization varchar(255) NOT NULL,
    location       varchar(255) NOT NULL
);

CREATE TABLE if not exists RECEPTIONIST
(
    rec_id        serial PRIMARY KEY,
    name          varchar(255) NOT NULL,
    working_hours varchar(255) NOT NULL
);

CREATE TABLE if not exists APPOINTMENT
(
    patient_id    bigint(20) unsigned NOT NULL,
    rec_id        bigint(20) unsigned NOT NULL,
    doctor_id     bigint(20) unsigned NOT NULL,
    ap_id         serial UNIQUE,
    date_and_time timestamp           NOT NULL,
    FOREIGN KEY (patient_id)
        REFERENCES PATIENT (id)
        ON DELETE CASCADE,
    FOREIGN KEY (doctor_id)
        REFERENCES DOCTOR (id)
        ON DELETE CASCADE,
    FOREIGN KEY (rec_id)
        REFERENCES RECEPTIONIST (rec_id)
        ON DELETE CASCADE,
    PRIMARY KEY (ap_id, patient_id, doctor_id, rec_id)
);

CREATE TABLE if not exists STAFF_INVENTORY
(
    id           serial,
    staff_id     bigint(20) unsigned NOT NULL,
    inventory_id bigint(20) unsigned NOT NULL,
    FOREIGN KEY (staff_id)
        REFERENCES STAFF (st_id)
        ON DELETE CASCADE,
    FOREIGN KEY (inventory_id)
        REFERENCES INVENTORY (item_id)
        ON DELETE CASCADE,
    PRIMARY KEY (id, inventory_id)
);

CREATE TABLE if not exists PATIENT_INVENTORY
(
    pat_inv_id   serial UNIQUE       NOT NULL,
    patient_id   bigint(20) unsigned NOT NULL,
    inventory_id bigint(20) unsigned not null,
    FOREIGN KEY (patient_id)
        REFERENCES PATIENT (id)
        ON DELETE CASCADE,
    FOREIGN KEY (inventory_id)
        REFERENCES INVENTORY (item_id)
        ON DELETE CASCADE,
    PRIMARY KEY (pat_inv_id, patient_id, inventory_id)
);

CREATE TABLE if not exists DOCTOR_INVENTORY
(
    id           serial UNIQUE       NOT NULL,
    doctor_id    bigint(20) unsigned not null,
    inventory_id bigint(20) unsigned not null,
    FOREIGN KEY (doctor_id)
        REFERENCES DOCTOR (id)
        ON DELETE CASCADE,
    FOREIGN KEY (inventory_id)
        REFERENCES INVENTORY (item_id)
        ON DELETE CASCADE,
    PRIMARY KEY (inventory_id, doctor_id, id)
);

CREATE TABLE if not exists STAFF_CHAT
(
    id       serial UNIQUE       NOT NULL,
    chat_id  varchar(255)        NOT NULL,
    staff_id bigint(20) unsigned NOT NULL,
    FOREIGN KEY (chat_id)
        REFERENCES CHAT (name)
        ON DELETE CASCADE,
    FOREIGN KEY (staff_id)
        REFERENCES STAFF (st_id)
        ON DELETE CASCADE,
    PRIMARY KEY (id, chat_id, staff_id)
);

CREATE TABLE if not exists DOCTOR_CHAT
(
    id        serial UNIQUE       NOT NULL,
    chat_id   varchar(255)        NOT NULL,
    doctor_id bigint(20) unsigned not null,
    FOREIGN KEY (chat_id)
        REFERENCES CHAT (name)
        ON DELETE CASCADE,
    FOREIGN KEY (doctor_id)
        REFERENCES DOCTOR (id)
        ON DELETE CASCADE,
    PRIMARY KEY (doctor_id, chat_id, id)
);

CREATE TABLE if not exists CHAT_RECEPTIONIST
(
    id              serial UNIQUE       NOT NULL,
    chat_id         varchar(255)        NOT NULL,
    receptionist_id bigint(20) unsigned NOT NULL,
    FOREIGN KEY (chat_id)
        REFERENCES CHAT (name)
        ON DELETE CASCADE,
    FOREIGN KEY (receptionist_id)
        REFERENCES RECEPTIONIST (rec_id)
        ON DELETE CASCADE,
    PRIMARY KEY (id, chat_id, receptionist_id)
);

CREATE TABLE if not exists RECEPTIONIST_AMBULANCE
(
    id              serial UNIQUE       NOT NULL,
    ambulance_id    bigint(20) unsigned NOT NULL,
    receptionist_id bigint(20) unsigned NOT NULL,
    FOREIGN KEY (ambulance_id)
        REFERENCES AMBULANCE (amb_id)
        ON DELETE CASCADE,
    FOREIGN KEY (receptionist_id)
        REFERENCES RECEPTIONIST (rec_id)
        ON DELETE CASCADE,
    PRIMARY KEY (id, receptionist_id, ambulance_id)
);

CREATE TABLE if not exists RECEPTIONIST_PATIENT
(
    id              serial UNIQUE       NOT NULL,
    patient_id      bigint(20) unsigned not NULL,
    receptionist_id bigint(20) unsigned NOT NULL,
    FOREIGN KEY (patient_id)
        REFERENCES PATIENT (id)
        ON DELETE CASCADE,
    FOREIGN KEY (receptionist_id)
        REFERENCES RECEPTIONIST (rec_id)
        ON DELETE CASCADE,
    PRIMARY KEY (id, patient_id, receptionist_id)
);