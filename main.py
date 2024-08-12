# основная точка входа для пользователя
from config import config
from src.utils import create_database

def main():
    params = config()
    create_database('course_work_5', params)


if __name__ == '__main__':
    main()