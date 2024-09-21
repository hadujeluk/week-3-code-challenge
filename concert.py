import sqlite3

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    @staticmethod
    def band(concert_id, conn):
        sql = """
        SELECT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = ?;
        """
        return conn.execute(sql, (concert_id,)).fetchone()

    @staticmethod
    def venue(concert_id, conn):
        sql = """
        SELECT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.id = ?;
        """
        return conn.execute(sql, (concert_id,)).fetchone()

    @staticmethod
    def hometown_show(concert_id, conn):
        sql = """
        SELECT CASE WHEN bands.hometown = venues.city THEN 1 ELSE 0 END
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?;
        """
        result = conn.execute(sql, (concert_id,)).fetchone()
        return bool(result[0]) if result else False

    @staticmethod
    def introduction(concert_id, conn):
        sql = """
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?;
        """
        result = conn.execute(sql, (concert_id,)).fetchone()
        if result:
            city, band_name, hometown = result
            return f"Hello {city}! We are The Three Men Army and Sauti Sol  from {hometown}, Kenya"
        return "No introduction data found for this concert."
