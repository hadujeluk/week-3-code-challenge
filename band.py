import sqlite3

class Band:
    def __init__(self, band_id):
        self.band_id = band_id

    @staticmethod
    def concerts(band_id, conn):
        sql = """
        SELECT concerts.* FROM concerts
        WHERE band_id = ?;
        """
        return conn.execute(sql, (band_id,)).fetchall()

    @staticmethod
    def venues(band_id, conn):
        sql = """
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = ?;
        """
        return conn.execute(sql, (band_id,)).fetchall()

    @staticmethod
    def play_in_venue(band_id, venue_id, date, conn):
        sql = """
        INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?);
        """
        conn.execute(sql, (band_id, venue_id, date))
        conn.commit()

    @staticmethod
    def all_introductions(band_id, conn):
        sql = """
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?;
        """
        concerts = conn.execute(sql, (band_id,)).fetchall()
        return [f"Hello {city}!!!!! We are {band_name} and we're from {hometown}" for city, band_name, hometown in concerts]

    @staticmethod
    def most_performances(conn):
        sql = """
        SELECT bands.*, COUNT(concerts.id) AS concert_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1;
        """
        return conn.execute(sql).fetchone()
