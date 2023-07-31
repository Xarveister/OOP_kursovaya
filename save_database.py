import psycopg2

from api_hh import API_hh
from config import config

data = API_hh()
params = config()


def get_data():
    """Получение данных из файла json"""
    vacancy_data = []
    employer_data = []
    for x in data:
        for values in x:
            vacancy_id = values['id']
            vacancy_name = values['name']
            published_date = values['published_at']
            salary_from = values['salary']['from'] if values['salary'] else None
            salary_to = values['salary']['to'] if values['salary'] else None
            url = values['url']
            employer_id = values['employer']['id']
            name = values['employer']['name']

            vacancy_data.append(
                (
                    vacancy_id,
                    vacancy_name,
                    published_date,
                    salary_from,
                    salary_to,
                    url,
                    employer_id
                )
            )

            employer_data.append(
                (
                    employer_id,
                    name
                )
            )
    return vacancy_data, employer_data


def save_database(database_name: str, params: dict):
    """Функция сохранения данных в таблицы"""
    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
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
                employer_id int REFERENCES employers(employer_id) ON UPDATE CASCADE
        )


        """)
    cur.execute('TRUNCATE vacancies RESTART IDENTITY CASCADE')
    cur.execute('TRUNCATE employers RESTART IDENTITY CASCADE')
    vacancies_data = get_data()[0]
    employer_data = get_data()[-1]

    cur.executemany("""INSERT INTO employers VALUES (%s, %s) ON CONFLICT (employer_id) DO NOTHING;""", employer_data)
    cur.executemany("""INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_id) DO NOTHING""",
                    vacancies_data)

    cur.close()
    conn.close()

