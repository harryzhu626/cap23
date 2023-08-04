import sqlite3
from typing import Iterable

# connecting to the database
connection = sqlite3.connect("cap23")
cursor = connection.cursor()

sql_create_table = '''
    CREATE TABLE IF NOT EXISTS opinions (
    id INTEGER PRIMARY KEY,
    comment_sentences TEXT, 
    opinions TEXT,
    comments TEXT, 
    comment_upvote INTEGER, 
    comment_date TEXT,
    comment_links TEXT,
    submission_title TEXT, 
    submission_upvote INTEGER
    )
'''
 
# execute the statement
cursor.execute(sql_create_table)
connection.commit()
insert_query = "INSERT INTO opinions \
        (comment_sentences, opinions, comments, comment_upvote, comment_date, comment_links, submission_title, submission_upvote) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"


def sql_multi_insert(sub_opinions_infos: Iterable):
    print(f'sql multi insert')
    connection_m = sqlite3.connect('cap23')
    cursor = connection_m.cursor()

    for sub in sub_opinions_infos:
        cursor.executemany(insert_query, sub)

    connection_m.commit()

    cursor.close()
    connection_m.close()

    # for pair in opinions_infos:
    #     print(f'iterable thru opinions')
    #     sql_single_insert(pair[0], pair[1])
    # connection_m.commit()

    # cursor.close()
    # connection_m.close()
    # print(f'closed')

def sql_query_k(query_size_k):
    connection_q = sqlite3.connect('cap23')
    cursor = connection_q.cursor()

    cursor.execute("SELECT * FROM documents LIMIT ?", (query_size_k,))
    results = cursor.fetchall()
    connection_q.close()
    return results