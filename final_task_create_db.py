import sqlite3

# Connect to the database, creating it if it doesn't exist
conn = sqlite3.connect('city_coordinates.db')

# If it's a new database, create the table
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS city (
        id INTEGER PRIMARY KEY,
        name TEXT,
        latitude REAL,
        longitude REAL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
