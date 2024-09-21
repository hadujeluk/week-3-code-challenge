import sqlite3

def create_tables():
    conn = sqlite3.connect('concerts.db')
    cur = conn.cursor()

    # Create bands table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hometown TEXT NOT NULL
    )
    ''')

    # Create venues table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        city TEXT NOT NULL
    )
    ''')

    # Create concerts table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER,
        venue_id INTEGER,
        date TEXT,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(venue_id) REFERENCES venues(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
