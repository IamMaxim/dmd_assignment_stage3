-- 1

create or replace function get_patients_appointments_today(patient_id int) returns setof appointment as $$
    select * from appointment where patient_id = $1 and date_and_time >= now()::date;
$$ language sql;

create or replace function get_doctors_from_appointments(appointments setof appointment) returns setof doctor as $$
    select * from doctor join $1 ON doctor.id;
$$ language sql;

create or replace function first_query(patient_id int, first_letter char(1), second_letter char(1)) returns setof doctor as $$
;
$$ language sql;

