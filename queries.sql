CREATE TABLE IF NOT EXISTS employers(
            employer_id int PRIMARY KEY,
            name varchar(255) NOT NULL)


CREATE TABLE IF NOT EXISTS vacancies(
            vacancy_id int PRIMARY KEY,
            vacancy_name varchar(255) NOT NULL,
            published_date date,
            salary_from int,
            salary_to int,
            url text NOT NULL,
            employer_id int REFERENCES employers(employer_id) ON UPDATE CASCADE)