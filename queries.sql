-- 1

create or replace function get_patients_appointments_today(patient_id int) returns setof appointment as
$$
select *
from appointment
where patient_id = $1
  and date_and_time >= now()::date;
$$ language sql;

create or replace function first_query(patient_id int, first_letter char(1), second_letter char(1)) returns setof varchar as
$$
select name
from (select name
      from (doctor
               join (
          select ap_id
          from get_patients_appointments_today($1) as app) as "$1ai" ON doctor.id = ap_id)) as "d$1a*"
where starts_with(split_part(name, ' ', 1), first_letter)::int +
      starts_with(split_part(name, ' ', 1), second_letter)::int +
      starts_with(split_part(name, ' ', 2), first_letter)::int +
      starts_with(split_part(name, ' ', 2), second_letter)::int = 1
$$
    language sql;


-- 2


-- 3

-- Returns the amount of appointments between the specified timestamps.
create or replace function number_of_appointments_between(patient_id int, after timestamp, before timestamp) returns bigint as
$$
select count(*)
from appointment
where patient_id = $1
  and date_and_time >= $2
  and date_and_time < $3
$$
    language sql;

create or replace function third_query() returns patient as
$$
select *
from patient
where number_of_appointments_between(id,
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month)
                                               as after1),
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '7' day)
                                               as before1)) >= 2
  and number_of_appointments_between(id,
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '7' day)
                                               as after2),
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '14' day)
                                               as before2)) >= 2
  and number_of_appointments_between(id,
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '14' day)
                                               as after3),
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '21' day)
                                               as before3)) >= 2
  and number_of_appointments_between(id,
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '21' day)
                                               as after4),
                                     (select *
                                      from date_trunc('month', current_date - interval '1' month + interval '28' day)
                                               as before4)) >= 2;
$$
    language sql;

-- 4
create or replace function prev_month_appointments() returns appointment as
$$
select *
from appointment
where date_and_time >= (select *from date_trunc('month', current_date - interval '1' month))
  and date_and_time < (select *from date_trunc('month', current_date))
$$
    language sql;

-- Returns the amount of appointments in the last month for a patient.
create or replace function number_of_appointments_between(patient_id int, after timestamp, before timestamp) returns bigint as
$$
select count(*)
from appointment
where patient_id = $1
  and date_and_time >= $2
  and date_and_time < $3
$$
    language sql;

create or replace function price_for(patient_id int) returns bigint as
$$
select case
           when number_of_appointments_between >= 3 and age >= 50 then 500 * number_of_appointments_between
           when number_of_appointments_between >= 3 and age < 50 then 250 * number_of_appointments_between
           when number_of_appointments_between < 3 and age >= 50 then 400 * number_of_appointments_between
           when number_of_appointments_between < 3 and age < 50 then 200 * number_of_appointments_between
           end as price
from (select *
      from number_of_appointments_between($1,
                                          date_trunc('month', current_date - interval '1' month),
                                          date_trunc('month', current_date)::timestamp),
          (select age
           from patient
           where id = $1) as "age") as "apps_and_age"
$$
    language sql;

create or replace function fourth_query() returns int as
$$
select sum(price_for(id))
from patient
$$
    language sql;


-- 5

