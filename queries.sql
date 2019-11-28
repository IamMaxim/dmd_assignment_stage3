-- 1

create or replace function get_patients_appointments_today(patient_id int) returns setof appointment as
$$
select *
from appointment
where patient_id = $1
  and date_and_time >= now()::date;
$$ language sql;

create or replace function get_last_patients_appointment(patient_id int) returns setof appointment as
$$
select *
from appointment
where patient_id = $1
order by date_and_time desc
limit 1;
$$ language sql;

create or replace function get_data_for_first_query(out p_id int, out d_name varchar(255)) as
$$
select (p.id, d.name)
from ((appointment join patient p on appointment.patient_id = p.id)
         join doctor d on appointment.doctor_id = d.id);
$$
    language sql;

create or replace function first_query(patient_id int, first_letter char(1), second_letter char(1)) returns setof varchar as
$$
select name
from (select name
      from (doctor
               join (
          select doctor_id
          from get_last_patients_appointment($1) as app) as "$1ai" ON doctor.id = doctor_id)) as "d$1a*"
where starts_with(split_part(name, ' ', 1), first_letter)::int +
      starts_with(split_part(name, ' ', 1), second_letter)::int +
      starts_with(split_part(name, ' ', 2), first_letter)::int +
      starts_with(split_part(name, ' ', 2), second_letter)::int = 1
$$
    language sql;


-- 2
create type second_query_result as (timeslot timestamp, count bigint);

create or replace function second_query() returns setof second_query_result as
$$
select appointment.date_and_time, count(appointment)
from appointment
where date_and_time >= date_trunc('year', current_date - interval '1' year)
  and date_and_time < date_trunc('year', current_date)
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

create or replace function get_prev_month() returns timestamp as
$$
select cast(date_trunc('month', current_date) as date) - interval '1' month
$$
    language sql;

create or replace function third_query() returns patient as
$$
select *
from (
         select *
         from patient
         where number_of_appointments_between(
                       id,
                       (select get_prev_month()),
                       (select get_prev_month() + interval '7' day)
                   ) >= 2
           and number_of_appointments_between(id,
                                              (get_prev_month() + interval '7' day),
                                              (select get_prev_month() + interval '14' day)
                   ) >= 2
           and number_of_appointments_between(id,
                                              (get_prev_month() + interval '14' day),
                                              (select get_prev_month() + interval '21' day)
                   ) >= 2
           and number_of_appointments_between(id,
                                              (get_prev_month() + interval '21' day),
                                              (select get_prev_month() + interval '28' day)
                   ) >= 2
     ) as result3;
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
-- create or replace function fifth_query(period int, patients_per_year int, total_patients int) returns setof doctor as
-- $$
-- SELECT doctor.* /*, patients*/
-- FROM (
--          SELECT noapy.doctor_id, SUM(noapy.ct) as patients
--          FROM (
--                   SELECT dp.doctor_id, COUNT(dp.patient_id) as ct, dp.dp
--                   FROM (
--                            SELECT a.patient_id, a.doctor_id, date_part('year', a.date_and_time) as dp
--                            FROM appointment as a,
--                                 doctor as d
--                            WHERE date_part('year', a.date_and_time) >
--                                  date_part('year', current_date) - period
--                              AND a.doctor_id = d.id
--                        ) as dp
--                   GROUP BY dp.doctor_id, dp.dp
--                   HAVING COUNT(dp.doctor_id) >= patients_per_year
--               ) as noapy
--          GROUP BY noapy.doctor_id
--          HAVING COUNT(noapy.ct) >= period
--             AND SUM(noapy.ct) > total_patients
--      ) as result,
--      doctor
-- WHERE result.doctor_id = doctor.id
--
-- $$ language sql;

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
                                 date_part('year', current_date) - 10
                             AND a.doctor_id = d.id
                       ) as dp
                  GROUP BY dp.doctor_id, dp.dp
                  HAVING COUNT(dp.doctor_id) >= 10
              ) as noapy
         GROUP BY noapy.doctor_id
         HAVING COUNT(noapy.ct) >= 10
            AND SUM(noapy.ct) > 100
     ) as result,
     doctor
WHERE result.doctor_id = doctor.id

$$ language sql;