import sqlite3

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    @staticmethod
    def concerts(venue_id, conn):
        sql = """
        SELECT concerts.* FROM concerts
        WHERE venue_id = ?;
        """
        return conn.execute(sql, (venue_id,)).fetchall()

    @staticmethod
    def bands(venue_id, conn):
        sql = """
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?;
        """
        return conn.execute(sql, (venue_id,)).fetchall()

    @staticmethod
    def concert_on(venue_id, date, conn):
        sql = """
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1;
        """
        return conn.execute(sql, (venue_id, date)).fetchone()

    @staticmethod
    def most_frequent_band(venue_id, conn):
        sql = """
        SELECT bands.*, COUNT(concerts.id) AS concert_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1;
        """
        return conn.execute(sql, (venue_id,)).fetchone()
