from configparser import ConfigParser
import psycopg2

def config(filename="database.ini"):
    '''коннектор для соединения с БД. при вызове можно передать другие аргументы '''
    config = ConfigParser()
    config.read(filename)
    database_config = dict(config.items('database'))
    conn = psycopg2.connect(
        host=database_config['host'],
        database=database_config['database'],
        user=database_config['user'],
        password=database_config['password'],
        port=database_config['port'],
    )
    return conn