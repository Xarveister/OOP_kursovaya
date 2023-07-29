import psycopg2
from config import config

params = config()


def create_database(database_name: str, params: dict):
    """Функция создания бзы данных и таблиц"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE  {database_name}")
    conn.commit()
    conn.close()

