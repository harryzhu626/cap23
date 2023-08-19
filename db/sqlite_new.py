import sqlite3

connection = sqlite3.connect('cap')
cursor = connection.cursor()

"""
table_movies
id  title   score   ratio   link                       
m1  Mady    100     0.9     reddit.com/r/movies/fjdfd  

table_comments
id      content         score   date    link                            movie
c1      'good. not bad' 10      1/2/23  reddit.com/r/movies/fjdfd/dkfd  m1

table_sentences
id      content     opinion     aspect  comment
s1      'good'      'positive'          c1
"""

submission_schema = '''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT, 
        score INTEGER, 
        link TEXT
    );
'''

comment_schema = '''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        content TEXT,
        score INTEGER,
        date TEXT,
        link TEXT,
        FOREIGN KEY (movie_id) REFERENCES movies (id)
    );
'''

sentence_schema = '''
    CREATE TABLE IF NOT EXISTS sentences (
        id INTEGER PRIMARY KEY,
        comment_id INTEGER, 
        content TEXT,
        opinion TEXT,
        aspect TEXT,
        FOREIGN KEY (comment_id) REFERENCES comments (id)
    );
'''

insert_query_movie = "INSERT INTO movies \
        (title, score, link) \
        VALUES (?, ?, ?)"

insert_query_comment = "INSERT INTO comments \
        (movie_id, content, score, date, link) \
        VALUES (?, ?, ?, ?, ?)"

insert_query_sentence = "INSERT INTO sentences \
        (comment_id, content, opinion, aspect) \
        VALUES (?, ?, ?, ?)"

cursor.execute(submission_schema)
cursor.execute(comment_schema)
cursor.execute(sentence_schema)

def insert_comment(cursor, comments, movie_id):
    print('movie id: ', movie_id)
    for comment, sentences in comments:
        cursor.execute(insert_query_comment, (movie_id, comment[0], comment[1], comment[2], comment[3]))
        comment_id = cursor.lastrowid
        for sentence in sentences:
            cursor.execute(insert_query_sentence, (comment_id, sentence[0], sentence[1], sentence[2]))


def sql_insert(movie, comments):
    connection_insert = sqlite3.connect('cap23')
    cursor = connection_insert.cursor()

    cursor.execute(insert_query_movie, movie)
    movie_id = cursor.lastrowid
        
    insert_comment(cursor, comments, movie_id)

    connection_insert.commit()

    cursor.close()
    connection_insert.close()


def sql_query_k(columns, table_name, query_size_k):
    connection_q = sqlite3.connect('cap23')
    cursor = connection_q.cursor()

    query_string = f"SELECT {columns} FROM {table_name} LIMIT {query_size_k};"
    cursor.execute(query_string)
    results = cursor.fetchall()
    cursor.close()
    connection_q.close()
    return results


def sql_query_entities():
    connection_q = sqlite3.connect('cap23')
    cursor = connection_q.cursor()
    query_entities = """
        SELECT title 
        FROM movies; 
    """
    cursor.execute(query_entities)
    results = cursor.fetchall()
    return results


def sql_query_join(movie_name):
    connection_q = sqlite3.connect('cap23')
    cursor = connection_q.cursor()

    query_join_string = f"""
        SELECT sentences.opinion, comments.date
        FROM sentences
        INNER JOIN comments ON sentences.comment_id = comments.rowid
        INNER JOIN movies ON comments.movie_id = movies.rowid
        WHERE movies.title = '{movie_name}';
    """
    
    cursor.execute(query_join_string)
    results = cursor.fetchall()
    cursor.close()
    connection_q.close()
    return results