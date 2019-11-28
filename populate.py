from populator import *
from random import *
from populator import gen_sex_and_name

# implemented line 49
medfile_against_patient = {}

# ==> Filling PATIENT
num_of_patients = 200

f = open("insert_script.sql", "w+")

snns = create_snn()
patient_names = {}
pat_ids = list(range(1, num_of_patients+1))
for patient in range(num_of_patients):
    ins_sex, ins_full_name = gen_sex_and_name()
    snn = snns.pop()
    ins_age = randint(0, 100)
    patient_names[patient+1] = ins_full_name
    f.write("INSERT INTO patient(age, sex, full_name, ssn) VALUES (%s, %s, '%s', %s);\n" % (
    ins_age, ins_sex, ins_full_name, snn))

f.write('\n')
print("Added", num_of_patients, "to PATIENT")

# ==> Filling DIGITAL_MEDICAL_FILE
num_of_reg_number = 0
num_of_prev_medical_files = 0
for curr_patient in range(1, num_of_patients + 1):
    reg_numbers = []
    num_of_files = randint(2, 4)
    for file in range(num_of_files):
        num_of_reg_number += 1
        reg_numbers.append(num_of_reg_number)

        ins_date_of_creation = gen_date().date()

        ins_patient_id = curr_patient

        # dictionary
        medfile_against_patient[num_of_reg_number] = ins_patient_id

        f.write(
            "INSERT INTO digital_medical_file(reg_number, date_of_creation, patient_id) VALUES (%s, '%s', %s);\n" % (
                num_of_reg_number,
                ins_date_of_creation,
                ins_patient_id))

    # Filling NUMBERS_OF_PREV_MEDICAL_FILES

    if num_of_files > 2:
        ins_file_id = reg_numbers[0]
        ins_prev_file_id = choice(reg_numbers[1:])
        num_of_prev_medical_files += 1

        f.write("INSERT INTO numbers_of_prev_medical_files(file_id, prev_file_id) VALUES (%s, %s);\n" % (ins_file_id,
                                                                                                         ins_prev_file_id))

f.write('\n')
print("Added", num_of_reg_number, "to DIGITAL_MEDICAL_FILE")
print("Added", num_of_prev_medical_files, "to NUMBERS_OF_PREV_MEDICAL_FILES")

# ==> Filling DIAGNOSE
for curr_reg_number in range(1, num_of_reg_number + 1):
    num_of_diagnoses = randint(0, 10)
    for diagnose in range(0, num_of_diagnoses):
        ins_id = choice(diagnose_name)

        # time is important for heart attacks for example
        ins_found_date = gen_date()

        # can be null
        ins_get_well_date = gen_date_later(ins_found_date)

        ins_reg_number = curr_reg_number

        ins_patient_id = medfile_against_patient.get(curr_reg_number)
        if ins_patient_id is None:
            break

        ins_treatment = choice(diagnose_treatment)

        # if person is well
        if gen_boolean():
            f.write(
                "INSERT INTO diagnose(name, found_date, get_well_date, reg_number, patient_id, treatment) VALUES ('%s', '%s', '%s', %s, %s, '%s');\n" %
                (ins_id, ins_found_date, ins_get_well_date, ins_reg_number, ins_patient_id, ins_treatment))
        else:
            f.write(
                "INSERT INTO diagnose(name, found_date, get_well_date, reg_number, patient_id, treatment) VALUES ('%s', '%s', 'null', %s, %s, '%s');\n" %
                (ins_id, ins_found_date, ins_reg_number, ins_patient_id, ins_treatment))

print("Finished filling DIAGNOSE")
f.write('\n')

# ==> Filling MED_TEST
for curr_reg_number in range(1, num_of_reg_number + 1):
    num_of_tests = randint(0, 3)
    for test in range(0, num_of_tests):

        # time is important as results norm may vary from it
        ins_collection_date = gen_date()

        ins_results_available = gen_boolean()

        if ins_results_available is False:
            ins_results = 'null'
        else:
            ins_results = choice(analyze_result)

        ins_reg_number = curr_reg_number

        ins_patient_id = medfile_against_patient.get(curr_reg_number)

        if ins_patient_id is None:
            break

        if ins_results == 'null':
            f.write(
                "INSERT INTO med_test(collection_date, results_available, results, reg_number, patient_id) VALUES ('%s', %s, %s, %s, %s);\n" %
                (ins_collection_date, ins_results_available, ins_results, ins_reg_number, ins_patient_id))
        else:
            f.write(
                "INSERT INTO med_test(collection_date, results_available, results, reg_number, patient_id) VALUES ('%s', %s, '%s', %s, %s);\n" %
                (ins_collection_date, ins_results_available, ins_results, ins_reg_number, ins_patient_id))

print("Finished filling MED_TEST")
f.write('\n')

# ==> Filling INVENTORY
num_of_inventory = randint(30, 70)
for inventory in range(num_of_inventory):
    ins_id = choice(inventory_name)

    ins_price_to_sell = randint(5, 500)
    if random() < 0.2:
        ins_price_to_sell = None

    ins_instruction = choice(inventory_instruction)
    if ins_price_to_sell is None:
        f.write("INSERT INTO inventory(name, price_to_sell, instruction) VALUES ('%s', %s, '%s');\n" % (
            ins_id, 'null',
            ins_instruction))
    else:
        f.write("INSERT INTO inventory(name, price_to_sell, instruction) VALUES ('%s', %s, '%s');\n" % (
            ins_id, ins_price_to_sell,
            ins_instruction))

f.write('\n')
print("Added", num_of_inventory, "to INVENTORY")

# ==> Filling SUPPLIERS
for inventory in range(1, num_of_inventory + 1):
    num_of_suppliers = randint(1, 3)
    for curr_sup in range(0, num_of_suppliers):
        ins_item_id = inventory
        ins_supplier = choice(inventory_supplier)
        ins_price_to_buy = randint(3, 100)

        f.write("INSERT INTO suppliers(item_id, supplier, price_to_buy) VALUES (%s, '%s', %s);\n" % (
            ins_item_id, ins_supplier,
            ins_price_to_buy))

f.write('\n')
print("Finished filling SUPPLIERS")

# ==> Filling STAFF
num_of_staff = randint(20, 30)
staff_ids = list(range(1, num_of_staff + 1))
for staff in range(num_of_staff):
    ins_staff_position = choice(staff_position)
    ins_sex, staff_name = gen_sex_and_name()

    f.write("INSERT INTO staff(position, name) VALUES ('%s', '%s' );\n" % (ins_staff_position, staff_name))

f.write('\n')
print("Added", num_of_staff, "to STAFF")

# ==> Filling DOCTOR
num_of_doctors = randint(10, 30)
license_ids = sample(range(100000, 999999), num_of_doctors)
doc_ids = list(range(1, num_of_doctors + 1))
for doctor in range(num_of_doctors):
    _, ins_full_name = gen_sex_and_name()

    working_hours_from, working_hours_to = gen_working_hours(randint(1, 3))
    ins_working_hours = working_hours_from.strftime('%H:%M:%S') + "; " + working_hours_to.strftime('%H:%M:%S')

    ins_specialization = ', '.join(sample(doc_specialization, randint(1, 3)))

    ins_license_id = license_ids.pop()

    f.write("INSERT INTO doctor(working_hours, specialization, name, license_id) VALUES ('%s', '%s', '%s', %s);\n" %
            (ins_working_hours, ins_specialization, ins_full_name, ins_license_id))

f.write('\n')
print("Added", num_of_doctors, "to DOCTOR")

# ==> Filling AMBULANCE
num_of_amb = randint(5, 10)
amb_ids = []
all_amb_ids = list(range(1, num_of_amb + 1))
for amb in range(1, num_of_amb + 1):
    ins_assigned = gen_boolean()

    ins_specialization = choice(doc_specialization)

    ins_location = choice(amb_loc)

    f.write("INSERT INTO ambulance(assigned, specialization, location) VALUES (%s, '%s', '%s');\n" % (ins_assigned,
                                                                                                      ins_specialization,
                                                                                                      ins_location))
    if not ins_assigned:
        amb_ids.append(amb)

print('\n')
print("Added", num_of_amb, "to AMBULANCE")

# ==> Filling RECEPTIONIST
num_of_rec = randint(3, 8)
rec_ids = list(range(1, num_of_rec + 1))
for rec in range(num_of_rec):
    _, rec_name = gen_sex_and_name()

    working_hours_from, working_hours_to = gen_working_hours(randint(1, 3))
    ins_working_hours = working_hours_from.strftime('%H:%M:%S') + "; " + working_hours_to.strftime('%H:%M:%S')

    f.write("INSERT INTO receptionist(name, working_hours) VALUES ('%s', '%s');\n" % (rec_name, ins_working_hours))

f.write('\n')
print("Added", num_of_rec, "to RECEPTIONIST")

# ==> Filling home visit APPOINTMENT
num_of_app = randint(1000, 2000)
for app in range(num_of_app):
    ins_patient_id = randint(1, num_of_patients)
    ins_rec_id = randint(1, num_of_rec)
    ins_doctor_id = randint(1, num_of_doctors)
    ins_date_and_time = gen_date()

    f.write("INSERT INTO appointment(patient_id, rec_id, doctor_id, date_and_time, is_home_visit) VALUES (%s, %s, %s, '%s', '%s');\n" %
            (ins_patient_id, ins_rec_id, ins_doctor_id, ins_date_and_time, gen_boolean()))

f.write('\n')
print("Added", num_of_app, "to APPOINTMENT")


# ==> Filling STAFF_INVENTORY
num_of_staff_inv = randint(10, num_of_inventory)
for inv in range(num_of_staff_inv):
    ins_staff_id = randint(1, num_of_staff)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write("INSERT INTO staff_inventory(staff_id, inventory_id) VALUES (%s, %s);\n" % (ins_staff_id, ins_inventory_id))

print("Added", num_of_staff_inv, "to STAFF_INVENTORY")
f.write('\n')

# ==> Filling PATIENT_INVENTORY
num_of_pat_inv = randint(10, num_of_inventory)
for inv in range(num_of_pat_inv):
    ins_patient_id = randint(1, num_of_patients)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write("INSERT INTO patient_inventory(patient_id, inventory_id) VALUES (%s, %s);\n" % (
        ins_patient_id, ins_inventory_id))

f.write('\n')
print("Added", num_of_pat_inv, "to PATIENT_INVENTORY")

# ==> Filling DOCTOR_INVENTORY
num_of_doc_inv = randint(10, num_of_inventory)
for inv in range(num_of_doc_inv):
    ins_doctor_id = randint(1, num_of_doctors)

    ins_inventory_id = randint(1, num_of_inventory)

    f.write(
        "INSERT INTO doctor_inventory(doctor_id, inventory_id) VALUES (%s, %s);\n" % (ins_doctor_id, ins_inventory_id))

f.write('\n')
print("Added", num_of_doc_inv, "to DOCTOR_INVENTORY")

added_chat_names = []


#todo redo chats and add chats with patient using patient_names


# ==> Filling CHAT
# ==> Filling STAFF_CHAT
num_of_staff_inv = randint(5, 20)

#todo refactoring starts here

num_of_chats = randint(5, 100)
amb_chats = 5
gen_chats = 10
doctor_chats = 10

def create_chat(id):
    whose = randint(1,5)
    global doctor_chats
    global gen_chats
    global amb_chats
    if whose ==1:
        if doctor_chats == 0:
            create_chat(id=id)
        else:
            doctor_chats -=1
            name = choice(chats_for_doctor)
            f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (id, name))
    if whose == 2:
        # patient_receptionist
        rec_id = choice(rec_ids, 1)
        patient_id = choice(pat_ids, 1)
        name = f'Chat with {patient_names.get(patient_id)}'
        f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (id, name))
        f.write("INSERT INTO receptionist_patient(patient_id, receptionist_id) VALUES (%s, %s);\n" % (patient_id,
                                                                                                  rec_id))
    if whose == 3:
        doc_id = choice(doc_ids, 1)
        patient_id = choice(pat_ids, 1)
        name = f'Chat with {patient_names.get(patient_id)}'
        f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (id, name))
        f.write(" INSERT INTO DOCTOR_PATIENT_CHAT (chat_id, doctor_id, patient_id) VALUES (%s, %s, %s);\n" %(id, doc_id, patient_id))
        #doctor_patient
    if whose == 4:
        # general
        #  todo to end with general chats
        if gen_chats == 0:
            create_chat(id=id)
        else:
            name = choice(chats_for_everybody)
            f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (id, name))
            for st_id in staff_ids:
                if gen_boolean():
                    f.write("INSERT INTO staff_chat(chat_id, staff_id) VALUES (%s, %s);\n" % (id, st_id))
            for doc in doc_ids:
                if gen_boolean():
                    f.write("INSERT INTO doctor_chat(chat_id, doctor_id) VALUES (%s, %s);\n" % (id, doc))
            for amb in all_amb_ids:
                if gen_boolean():
                    f.write("INSERT INTO chat_receptionist (chat_id, staff_id) VALUES (%s, %s);\n" % (id, amb))
    if whose == 5:
        if amb_chats == 0:
            create_chat(id=id)
        else:
            amb_chats -=1
            name = choice(chats_for_amb)
            f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (id, name))

            ambulance_id = sample(amb_ids, 1)
            receptionist_id = randint(0, num_of_rec)

            f.write("INSERT INTO receptionist_ambulance(ambulance_id, receptionist_id) VALUES (%s, %s);\n" % (ambulance_id,
                                                                                                      receptionist_id))


for chat_id in range(1, num_of_chats+1):
    create_chat(chat_id)

print("Added", num_of_chats, 'chats')

#todo refactoring ends here

# cur_chat_id = 1
# num_of_staff_chat = randint(1, 5)
# chat_ids = list(range(1, num_of_staff_chat + 1))
# for chat_id in range(1, num_of_staff_chat + 1):
#     chat_name = choice(chat_names)
#     f.write("INSERT INTO chat(chat_id, name) VALUES (%s,'%s');\n" % (cur_chat_id, chat_name))
#     chat_names.remove(chat_name)
#     added_chat_names.append(chat_name)
#     for id in staff_ids:
#         if gen_boolean():
#             f.write("INSERT INTO staff_chat(chat_id, staff_id) VALUES (%s, %s);\n" % (cur_chat_id, id))
#
#     cur_chat_id += 1
#
# f.write('\n')
# print("Added", num_of_staff_chat, "to STAFF_CHAT")

# ==> Filling CHAT
# ==> Filling DOCTOR_CHAT
# num_of_doctor_chat = randint(1, 5)
# for chat_id in range(num_of_doctor_chat):
#     curr_chat_name = choice(chat_names)
#     f.write("INSERT INTO chat(chat_id, name) VALUES (%s, '%s');\n" % (cur_chat_id, curr_chat_name))
#     chat_names.remove(curr_chat_name)
#     added_chat_names.append(curr_chat_name)
#
#     ins_chat_id = curr_chat_name
#     for id in doc_ids:
#         if gen_boolean():
#             f.write("INSERT INTO doctor_chat(chat_id, doctor_id) VALUES (%s, %s);\n" % (cur_chat_id, id))
#
#     cur_chat_id += 1
#
# print("Added", num_of_doctor_chat, "to DOCTOR_CHAT")
# f.write('\n')


# ==> Filling CHAT
# ==> Filling CHAT_RECEPTIONIST
# num_of_rec_chat = randint(1, 2)
# for chat_id in range(num_of_rec_chat):
#     curr_chat_name = choice(chat_names)
#     f.write("INSERT INTO chat(chat_id, name) VALUES (%s, '%s');\n" % (cur_chat_id, curr_chat_name))
#     chat_names.remove(curr_chat_name)
#     added_chat_names.append(curr_chat_name)
#
#     ins_chat_id = curr_chat_name
#     for id in rec_ids:
#         if gen_boolean():
#             f.write(
#                 "INSERT INTO chat_receptionist(chat_id, receptionist_id) VALUES ('%s', '%s');\n" % (cur_chat_id, id))
#     cur_chat_id += 1
#
# num_of_chats = num_of_staff_chat + num_of_doctor_chat + num_of_rec_chat
# f.write('\n')
# print("Added", num_of_rec_chat, "to CHAT_RECEPTIONIST")
# print("Added", num_of_chats, "to CHAT")

# ==> Filling MESSAGES
for chat_id in range(1, num_of_chats + 1):
    ins_id = chat_id
    num_of_messages = randint(0, 17)

    for message in range(num_of_messages):
        ins_messages = choice(chat_message)

        f.write("INSERT INTO messages(messages, chat_id) VALUES ('%s', %s);\n" % (ins_messages, ins_id))

f.write('\n')

# # ==> Filling RECEPTIONIST_AMBULANCE
# busy_ambs = amb_ids
# num_of_rec_amb = len(busy_ambs)
# for amb_i in range(num_of_rec_amb):
#     ins_ambulance_id = busy_ambs[amb_i]
#     ins_receptionist_id = randint(0, num_of_rec)
#
#     f.write("INSERT INTO receptionist_ambulance(ambulance_id, receptionist_id) VALUES (%s, %s);\n" % (ins_ambulance_id,
#                                                                                                       ins_receptionist_id))
#
# print("Finished filling RECEPTIONIST_AMBULANCE")
# f.write('\n')
#
# # ==> Filling RECEPTIONIST_PATIENT
# num_of_rec_pat = randint(num_of_patients // 2, num_of_patients)
# for rec_pat in range(num_of_rec_pat):
#     ins_patient_id = randint(1, num_of_patients)
#     ins_receptionist_id = randint(1, num_of_rec)
#
#     f.write("INSERT INTO receptionist_patient(patient_id, receptionist_id) VALUES (%s, %s);\n" % (ins_patient_id,
#                                                                                                   ins_receptionist_id))

# print("Finished filling RECEPTIONIST_PATIENT")
f.close()
