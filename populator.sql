insert into ambulance values (assigned, amd_id, specialization, location);
insert into appointment values (patient_id, rec_id, doctor_id, ap_id, date_and_time);
insert into chat values (name);
insert into chat_receptionist values (id, chat_id, receptionist_id);
insert into diagnose values (name, di_id, get_well_date, found_date, reg_number, patient_id, treatment);
insert into digital_medical_file values (reg_number, date_of_creation, patient_id);
insert into doctor values (working_hours, specialization, name, license_id);
insert into doctor_chat values (id, chat_id, doctor_id);
insert into doctor_inventory values (id, doctor_id, inventory_id);
insert into inventory values (item_id, name, price_to_sell, instruction);
insert into med_test values (res_id, collection_date, results_available, results, reg_number, patient_id);
insert into messages values (id, messages, name);
insert into numbers_of_prev_medical_files values (id, file_id, prev_file_id);
insert into patient values (age, sex, id, full_name);
insert into patient_inventory values (pat_inv_id, patient_id, inventory_id);
insert into receptionist values (rec_id, name, working_hours);
insert into receptionist_ambulance values (id, ambulance_id, receptionist_id);
insert into receptionist_patient values (id, patient_id, receptionist_id);
insert into staff values (st_id, position);
insert into staff_chat values (id, chat_id, staff_id);
insert into staff_inventory values (id ,staff_id, inventory_id);
insert into suppliers values (id, item_id, supplier, price_to_buy);


