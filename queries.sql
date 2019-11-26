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
create or replace function second_query(out timeslot timestamp, out count bigint) as
$$
select appointment.date_and_time, count(appointment)
from appointment
where date_and_time >= date_trunc('month', current_date - interval '1' month)
  and date_and_time < date_trunc('month', current_date)
group by appointment.date_and_time
$$ language sql;


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

create or replace function fourth_query() returns numeric as
$$
select sum(price_for(id))
from patient
$$
    language sql;


-- 5
create or replace function fifth_query() returns setof doctor as
$$
SELECT doctor.* /*, patients*/
FROM (
         SELECT noapy.doctor_id, SUM(noapy.ct) as patients
         FROM (
                  SELECT dp.doctor_id, COUNT(dp.patient_id) as ct, dp.dp
                  FROM (
                           SELECT a.patient_id, a.doctor_id, date_part('year', a.date_and_time) as dp
                           FROM appointment as a,
                                doctor as d
                           WHERE date_part('year', a.date_and_time) >
                                 date_part('year', current_date) - 10 -- How many years
                             AND a.doctor_id = d.id
                       ) as dp
                  GROUP BY dp.doctor_id, dp.dp
                  HAVING COUNT(dp.doctor_id) >= 5 -- How many appointments per year
              ) as noapy
         GROUP BY noapy.doctor_id
         HAVING COUNT(noapy.ct) >= 10 -- Equal to how many years
            AND SUM(noapy.ct) > 100 -- Num of all patients per this period of time
     ) as result,
     doctor
WHERE result.doctor_id = doctor.id

$$ language sql;