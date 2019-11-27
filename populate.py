from hospital_system.requests.sql_manager import update, execute
from populator import *
from random import *

update(open('SQL/table_creation.sql', 'r').read())

# Filling PATIENT

num_of_patients = 200

f = open("insert_script.txt", "w+")

for patient in range(1, num_of_patients + 1):
    ins_sex = gen_boolean()

    if ins_sex:
        ins_full_name = choice(fem_name) + ' ' + choice(surnames)
    else:
        ins_full_name = choice(male_name) + ' ' + choice(surnames)

    ins_age = randint(0, 100)

    f.write("INSERT INTO patient(age, sex, full_name) VALUES (%s, %s, %s);" % (ins_age, ins_sex, ins_full_name))

f.write('\n')
print("Added", num_of_patients, "to PATIENT")

# Filling DIGITAL_MEDICAL_FILE

num_of_reg_number = 1
num_of_prev_medical_files = 0
for curr_patient in range(1, num_of_patients + 1):
    reg_numbers = []
    num_of_files = randint(2, 4)
    for file in range(1, num_of_files + 1):
        reg_numbers.append(num_of_reg_number)
        num_of_reg_number += 1

        ins_date_of_creation = gen_date()

        ins_patient_id = curr_patient

        f.write(
            "INSERT INTO digital_medical_file(date_of_creation, patient_id) VALUES (%s, %s);" % (ins_date_of_creation,
                                                                                                 ins_patient_id))

    # Filling NUMBERS_OF_PREV_MEDICAL_FILES

    if num_of_files > 2:
        ins_file_id = reg_numbers[0]
        ins_prev_file_id = choice(reg_numbers[1:])
        num_of_prev_medical_files += 1

        f.write("INSERT INTO numbers_of_prev_medical_files(file_id, prev_file_id) VALUES (%s, %s);" % (ins_file_id,
                                                                                                       ins_prev_file_id))

print("Added", num_of_reg_number, "to DIGITAL_MEDICAL_FILE")
print("Added", num_of_prev_medical_files, "to NUMBERS_OF_PREV_MEDICAL_FILES")
f.write('\n')
# Filling DIAGNOSE

for curr_reg_number in range(1, num_of_reg_number):
    num_of_diagnoses = randint(0, 3)
    for diagnose in range(0, num_of_diagnoses):
        ins_name = choice(diagnose_name)

        ins_found_date = gen_date()

        ins_get_well_date = gen_date_later(ins_found_date)

        ins_reg_number = curr_reg_number

        ins_patient_id = execute("SELECT patient_id FROM digital_medical_file WHERE reg_number=%s", curr_reg_number)[0][
            0]

        ins_treatment = choice(diagnose_treatment)

        f.write(
            "INSERT INTO diagnose(name, found_date, get_well_date, reg_number, patient_id, treatment) VALUES (%s, %s, %s, %s, %s, %s);" %
            (ins_name, ins_found_date, ins_get_well_date, ins_reg_number, ins_patient_id, ins_treatment))

print("Finished filling DIAGNOSE")
f.write('\n')

# Filling MED_TEST

for curr_reg_number in range(1, num_of_reg_number):
    num_of_tests = randint(0, 3)
    for test in range(0, num_of_tests):
        ins_collection_date = gen_date()

        ins_results_available = gen_boolean()

        ins_results = choice(analyze_result)

        ins_reg_number = curr_reg_number

        ins_patient_id = execute("SELECT patient_id FROM digital_medical_file WHERE reg_number=%s", curr_reg_number)[0][
            0]

        f.write(
            "INSERT INTO med_test(collection_date, results_available, results, reg_number, patient_id) VALUES (%s, %s, %s, %s, %s);" %
            (ins_collection_date, ins_results_available, ins_results, ins_reg_number, ins_patient_id))

print("Finished filling MED_TEST")
f.write('\n')
# Filling INVENTORY

num_of_inventory = randint(30, 70)
for inventory in range(1, num_of_inventory + 1):
    ins_name = choice(inventory_name)

    ins_price_to_sell = randint(5, 500)
    if random() < 0.2:
        ins_price_to_sell = None

    ins_instruction = choice(inventory_instruction)

    f.write(
        "INSERT INTO inventory(name, price_to_sell, instruction) VALUES (%s, %s, %s);" % (ins_name, ins_price_to_sell,
                                                                                          ins_instruction))

print("Added", num_of_inventory, "to INVENTORY")
f.write('\n')
# Filling SUPPLIERS

for inventory in range(1, num_of_inventory + 1):
    num_of_suppliers = randint(1, 3)
    for curr_sup in range(0, num_of_suppliers):
        ins_item_id = inventory
        ins_supplier = choice(inventory_supplier)
        ins_price_to_buy = randint(3, 100)

        f.write(
            "INSERT INTO suppliers(item_id, supplier, price_to_buy) VALUES (%s, %s, %s);" % (ins_item_id, ins_supplier,
                                                                                             ins_price_to_buy))

print("Finished filling SUPPLIERS")
f.write('\n')
# Filling STAFF

num_of_staff = randint(20, 30)
for staff in range(1, num_of_staff + 1):
    ins_staff_position = choice(staff_position)
    ins_sex = gen_boolean()

    if ins_sex:
        staff_name = choice(fem_name) + ' ' + choice(surnames)
    else:
        staff_name = choice(male_name) + ' ' + choice(surnames)

    f.write("INSERT INTO staff(position) VALUES (%s, %s );" % (ins_staff_position, staff_name))

print("Added", num_of_staff, "to STAFF")
f.write('\n')
# Filling DOCTOR

num_of_doctors = randint(10, 30)
for doctor in range(1, num_of_doctors + 1):
    if gen_boolean():
        ins_full_name = choice(fem_name) + ' ' + choice(surnames)
    else:
        ins_full_name = choice(male_name) + ' ' + choice(surnames)

    working_hours_from, working_hours_to = gen_working_hours(randint(1, 3))
    ins_working_hours = working_hours_from.strftime('%H:%M:%S') + "; " + working_hours_to.strftime('%H:%M:%S')

    ins_specialization = ', '.join(sample(doc_specialization, randint(1, 3)))

    ins_license_id = randint(100000, 999999)

    f.write("INSERT INTO doctor(working_hours, specialization, name, license_id) VALUES (%s, %s, %s, %s);" %
            (ins_working_hours, ins_specialization, ins_full_name, ins_license_id))

print("Added", num_of_doctors, "to DOCTOR")
f.write('\n')
# Filling AMBULANCE

num_of_amb = randint(5, 10)
for amb in range(1, num_of_amb + 1):
    ins_assigned = gen_boolean()

    ins_specialization = choice(doc_specialization)

    ins_location = choice(amb_loc)

    f.write("INSERT INTO ambulance(assigned, specialization, location) VALUES (%s, %s, %s);" % (ins_assigned,
                                                                                               ins_specialization,
                                                                                               ins_location))

print("Added", num_of_amb, "to AMBULANCE")
print('\n')

# Filling RECEPTIONIST

num_of_rec = randint(3, 8)
for rec in range(1, num_of_rec + 1):
    if gen_boolean():
        ins_name = choice(fem_name) + " " + choice(surnames)
    else:
        ins_name = choice(male_name) + " " + choice(surnames)

    working_hours_from, working_hours_to = gen_working_hours(randint(1, 3))
    ins_working_hours = working_hours_from.strftime('%H:%M:%S') + "; " + working_hours_to.strftime('%H:%M:%S')

    f.write("INSERT INTO receptionist(name, working_hours) VALUES (%s, %s);" % (ins_name, ins_working_hours))

print("Added", num_of_rec, "to RECEPTIONIST")
f.write('\n')

# Filling APPOINTMENT

num_of_app = randint(1000, 2000)
for app in range(1, num_of_app + 1):
    ins_patient_id = randint(1, num_of_patients)
    ins_rec_id = randint(1, num_of_rec)
    ins_doctor_id = randint(1, num_of_doctors)
    ins_date_and_time = gen_date()

    f.write("INSERT INTO appointment(patient_id, rec_id, doctor_id, date_and_time) VALUES (%s, %s, %s, %s);" %
            (ins_patient_id, ins_rec_id, ins_doctor_id, ins_date_and_time))

print("Added", num_of_app, "to APPOINTMENT")
f.write('\n')

# Filling STAFF_INVENTORY

num_of_staff_inv = randint(10, num_of_inventory)
for inv in range(1, num_of_staff_inv + 1):
    ins_staff_id = randint(1, num_of_staff)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write("INSERT INTO staff_inventory(staff_id, inventory_id) VALUES (%s, %s);" % (ins_staff_id, ins_inventory_id))

print("Added", num_of_staff_inv, "to STAFF_INVENTORY")
f.write('\n')
# Filling PATIENT_INVENTORY

num_of_pat_inv = randint(10, num_of_inventory)
for inv in range(1, num_of_pat_inv + 1):
    ins_patient_id = randint(1, num_of_patients)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write(
        "INSERT INTO patient_inventory(patient_id, inventory_id) VALUES (%s, %s);" % (ins_patient_id, ins_inventory_id))

print("Added", num_of_pat_inv, "to PATIENT_INVENTORY")
f.write('\n')

# Filling DOCTOR_INVENTORY

num_of_doc_inv = randint(10, num_of_inventory)
for inv in range(1, num_of_doc_inv + 1):
    ins_doctor_id = randint(1, num_of_doctors)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write("INSERT INTO doctor_inventory(doctor_id, inventory_id) VALUES (%s, %s);" % (ins_doctor_id, ins_inventory_id))

print("Added", num_of_doc_inv, "to DOCTOR_INVENTORY")
f.write('\n')

chat_names = chat_name
added_chat_names = []

# Filling CHAT
# Filling STAFF_CHAT

num_of_staff_chat = randint(1, 2)
for chat in range(1, num_of_staff_chat + 1):
    curr_chat_name = choice(chat_names)
    f.write("INSERT INTO chat(name) VALUES (%s);" % (curr_chat_name))
    chat_names.remove(curr_chat_name)
    added_chat_names.append(curr_chat_name)

    ins_chat_id = curr_chat_name

    staff_ids = sample(execute("SELECT st_id FROM staff"), num_of_staff // 2)
    for id in staff_ids:
        f.write("INSERT INTO staff_chat(chat_name, staff_id) VALUES (%s, %s);" % (ins_chat_id, id[0]))

print("Added", num_of_staff_chat, "to STAFF_CHAT")
f.write('\n')
# Filling CHAT
# Filling DOCTOR_CHAT

num_of_doctor_chat = randint(1, 2)
for chat in range(1, num_of_doctor_chat + 1):
    curr_chat_name = choice(chat_names)
    f.write("INSERT INTO chat(name) VALUES (%s);" % curr_chat_name)
    chat_names.remove(curr_chat_name)
    added_chat_names.append(curr_chat_name)

    ins_chat_id = curr_chat_name

    doctor_ids = sample(execute("SELECT id FROM doctor"), num_of_doctors // 2)
    for id in doctor_ids:
        f.write("INSERT INTO doctor_chat(chat_id, doctor_id) VALUES (%s, %s);" % (ins_chat_id, id[0]))

print("Added", num_of_doctor_chat, "to DOCTOR_CHAT")
f.write('\n')
# Filling CHAT
# Filling CHAT_RECEPTIONIST

num_of_rec_chat = randint(1, 2)
for chat in range(1, num_of_rec_chat + 1):
    curr_chat_name = choice(chat_names)
    f.write("INSERT INTO chat(name) VALUES (%s);" % curr_chat_name)
    chat_names.remove(curr_chat_name)
    added_chat_names.append(curr_chat_name)

    ins_chat_id = curr_chat_name

    rec_ids = sample(execute("SELECT rec_id FROM receptionist"), num_of_rec // 2)
    for id in rec_ids:
        f.write("INSERT INTO chat_receptionist(chat_id, receptionist_id) VALUES (%s, %s);" % (ins_chat_id, id[0]))

num_of_chats = num_of_staff_chat + num_of_doctor_chat + num_of_rec_chat
print("Added", num_of_rec_chat, "to CHAT_RECEPTIONIST")
print("Added", num_of_chats, "to CHAT")
f.write('\n')

# Filling MESSAGES

for chat in range(1, num_of_chats + 1):
    ins_name = added_chat_names[chat - 1]

    num_of_messages = randint(0, 7)
    for message in range(0, num_of_messages):
        ins_messages = choice(chat_message)

        f.write("INSERT INTO messages(messages, name) VALUES (%s, %s);" % (ins_messages, ins_name))

f.write('\n')
# Filling RECEPTIONIST_AMBULANCE

busy_ambs = execute("SELECT amb_id FROM ambulance WHERE assigned=false")
num_of_rec_amb = len(busy_ambs)
itr = 0
for rec_amb in range(1, num_of_rec_amb + 1):
    ins_ambulance_id = busy_ambs[itr][0]

    itr += 1

    ins_receptionist_id = randint(1, num_of_rec)  # choice(execute("SELECT rec_id FROM receptionist"))[0][0]

    f.write("INSERT INTO receptionist_ambulance(ambulance_id, receptionist_id) VALUES (%s, %s);" % (ins_ambulance_id,
           ins_receptionist_id))

print("Finished filling RECEPTIONIST_AMBULANCE")
f.write('\n')
# Filling RECEPTIONIST_PATIENT

num_of_rec_pat = randint(num_of_patients // 2, num_of_patients)
for rec_pat in range(1, num_of_rec_pat):
    ins_patient_id = randint(1, num_of_patients)

    ins_receptionist_id = randint(1, num_of_rec)

    f.write("INSERT INTO receptionist_patient(patient_id, receptionist_id) VALUES (%s, %s);" % (ins_patient_id,
           ins_receptionist_id))

print("Finished filling RECEPTIONIST_PATIENT")
f.close()