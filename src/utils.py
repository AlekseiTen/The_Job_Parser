import psycopg2


def create_database(database: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о компаниях и вакансиях."""

    try:
        conn = psycopg2.connect(database=database, **params)
        conn.autocommit = True
        with conn.cursor() as cur:
            try:
                cur.execute(f"DROP DATABASE IF EXISTS {database}")
            except psycopg2.errors.ObjectInUse:
                print(f"Не удалось удалить базу данных {database}: она используется другим процессом.")
            cur.execute(f"CREATE DATABASE {database}")

    except psycopg2.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
        return

    try:
        conn = psycopg2.connect(database=database, **params)
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE employers (
                    employer_id INT PRIMARY KEY,
                    employer_name VARCHAR(255) NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE vacancies (
                    vacancy_id SERIAL PRIMARY KEY,
                    employer_id INT REFERENCES employers(employer_id),
                    vacancy_name VARCHAR(255) NOT NULL,
                    salary INT NOT NULL,
                    requirement TEXT,
                    vacancy_url VARCHAR(255) NOT NULL
                )
            """)

        conn.commit()
    except psycopg2.Error as e:
        print(f"Ошибка при создании таблиц: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()