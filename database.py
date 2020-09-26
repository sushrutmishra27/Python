import sqlite3


CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS BEANS(id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
INSERT_BEAN = "INSERT INTO BEANS(name, method, rating) VALUES(?, ?, ?);"
GET_ALL_BEANS = "SELECT * FROM BEANS;"
GET_BEANS_BY_NAME = "SELECT * FROM BEANS WHERE name = ?;"
GET_BEST_PREPARATION = """
SELECT * FROM BEANS
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
"""

def connect():
    return sqlite3.connect('data.db')

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, name, method, rating):
def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name,method,rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

def get_best_preparation(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION, (name,)).fetchone()
