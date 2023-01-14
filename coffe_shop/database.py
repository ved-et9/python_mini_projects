import sqlite3

CREATE_TABLE_BEANS="CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_BEAN= "INSERT INTO beans (name,method,rating) values(?,?,?);"

GET_ALL_BEANS="SELECT * FROM beans;"

GET_BEANS_BY_NAME="SELECT * FROM beans WHERE name= ?;"

GET_BEST_PREPARATION_FOR_BEAN="""
SELECT * FROM beans
WHERE name =?
ORDER BY rating DESC
LIMIT 1;"""

DROPDOWN_BEAN="""
DELETE FROM beans
WHERE name =?"""


#connect will return the connection with the database#
def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_BEANS)
    

def add_beans(connection,name,method,rating):
    with connection:
        connection.execute(INSERT_BEAN,(name,method,rating))



def get_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS)


def get_beans_by_name(connection,name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME,(name,)).fetchall()



def get_best_preparation_for_bean(connection,name):
    with connection:#                                            comma after name is necesaary if not it will ought to take all bindings with it such as (method and rating)#
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN,(name,)).fetchone()



def delete_entry(connection,name):
    with connection:
        return connection.execute(DROPDOWN_BEAN,(name,))

