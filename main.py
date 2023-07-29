from api_hh import API_hh
from database import create_database
from config import config
from save_database import save_database


def main():
    params = config()
    API_hh()
    create_database('Vacancy', params)
    save_database('Vacancy', params)

if __name__ == "__main__":
    main()