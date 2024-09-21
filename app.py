import sqlite3
from concert import Concert

def setup_database(conn):
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hometown TEXT NOT NULL
    )
    ''')
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        city TEXT NOT NULL
    )
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER NOT NULL,
        venue_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (band_id) REFERENCES bands(id),
        FOREIGN KEY (venue_id) REFERENCES venues(id)
    )
    ''')

    
    if conn.execute("SELECT COUNT(*) FROM bands").fetchone()[0] == 0:
        conn.execute("INSERT INTO bands (name, hometown) VALUES ('Broke Not Poor', 'Nairobi')")
        conn.execute("INSERT INTO bands (name, hometown) VALUES ('Wine and Blankets', 'Nairobi')")
        
        conn.execute("INSERT INTO venues (title, city) VALUES ('The Jyuce Party', 'Nairobi')")
        conn.execute("INSERT INTO venues (title, city) VALUES ('Sol Fest', 'Nairobi')")
        
        
        conn.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-05')")  
        conn.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-10-10')")  

def main():
    conn = sqlite3.connect('concerts.db')

    
    setup_database(conn)

    
    concert_id = 1  

    
    band = Concert.band(concert_id, conn)
    print(band)

    
    venue = Concert.venue(concert_id, conn)
    print(venue)
    is_hometown = Concert.hometown_show(concert_id, conn)
    print(f"Hometown show: {is_hometown}")

    intro = Concert.introduction(concert_id, conn)
    print(intro)

    conn.close()

if __name__ == "__main__":
    main()
