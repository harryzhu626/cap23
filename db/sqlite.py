import sqlite3
from typing import Iterable

# connecting to the database
connection = sqlite3.connect("cap23")
cursor = connection.cursor()

sql_create_table = '''CREATE TABLE IF NOT EXISTS opinions (
    id INTEGER PRIMARY KEY,
    submission TEXT, 
    comments TEXT, 
    opinions TEXT, 
    )'''
 
# execute the statement
cursor.execute(sql_create_table)
connection.close()


def sql_single_insert(opinion, cursor):
    
    cursor.execute(
        "INSERT INTO paragraphs \
        (paragraph, book, author, dialect, period) \
        VALUES (?, ?, ?, ?, ?)", 
        (,,,, )
    ) 


def sql_multi_insert(opinions: Iterable):
    connection_m = sqlite3.connect('cap23')
    cursor = connection_m.cursor()

    for opinion in opinions:
        sql_single_insert(opinion, cursor)
    connection_m.commit()


def sql_query_k(query_size_k):
    