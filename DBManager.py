import psycopg2
from config import config
params = config()
conn = psycopg2.connect(dbname=database_name, **params)
conn.autocommit = True
cur = conn.cursor()


class DBManager:
    """Класс для подключения к базе данных"""

    def __init__(self):
        self.cursor = cur

    def get_companies_and_vacancies_count(self):
        """Метод, который получает список всех компаний и количество вакансий"""
        self.cursor.execute("""
        SELECT name , COUNT(*) AS vacancies_count FROM employers
        LEFT JOIN vacancies USING(employer_id)
        GROUP BY name
        """)
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """Метод, который получает все вакансии с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        self.cursor.execute("""	     		
        SELECT vacancy_name, salary_from, salary_to, url FROM	vacancies
        FULL JOIN employers USING(employer_id)	
        """)
        return self.cursor.fetchall()

    def get_avg_salary(self):
        """Метод, который получает среднюю зарплату по вакансиям."""
        self.cursor.execute("""
        SELECT AVG(salary_from), AVG(salary_to) FROM vacancies
        WHERE salary_from>0 and salary_to>0
        """)
        return self.cursor.fetchall()

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий у которых зарплата выше средней"""
        self.cursor.execute("""
        SELECT * FROM vacancies 
        WHERE salary_from>(SELECT AVG(salary_from) FROM vacancies) 
        OR salary_to>(SELECT AVG(salary_to) FROM vacancies)
        """)
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, user_input):
        """Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        self.cursor.execute(f"""
        SELECT * FROM vacancies 
        WHERE vacancy_name LIKE '%{user_input}%'
        """)
        return self.cursor.fetchall()
