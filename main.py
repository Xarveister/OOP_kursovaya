from pprint import pprint

from DBManager import DBManager
from api_hh import API_hh
from database import create_database
from config import config
from save_database import save_database


def main():
    params = config()
    API_hh()
    create_database('Vacancy', params)
    save_database('Vacancy', params)
    db_manager = DBManager('Vacancy')
    pprint(db_manager.get_companies_and_vacancies_count())
    print('')
    pprint(db_manager.get_all_vacancies())
    print('')
    pprint(db_manager.get_avg_salary())
    print('')
    pprint(db_manager.get_vacancies_with_higher_salary())
    print('')
    pprint(db_manager.get_vacancies_with_keyword(user_input=input().title()))
    db_manager.close_db_connection()

if __name__ == "__main__":
    main()