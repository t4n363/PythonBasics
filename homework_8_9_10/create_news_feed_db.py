import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('db_feed.db')

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Create a table to store publications
cursor.execute('''
    CREATE TABLE IF NOT EXISTS t_news_feed (
        id INTEGER PRIMARY KEY,
        publication_type TEXT,
        publication_text TEXT,
        publication_city TEXT,
        publication_date DATETIME,
        publication_expiration DATETIME
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
