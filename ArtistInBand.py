import sqlite3

class artistinband:

    def __init__(self,artist,band):
        self.artist = artist
        self.band = band

    def addToDatabase(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("INSERT INTO artistinband (artist,band,artist_band) VALUES ( '" + self.artist + "' , '" + self.band + "' , '" + self.artist + self.band + "' ) ;")
        conn.commit()


    def DeleteArtistFromBand(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM artistinband WHERE( artist_band = '" + self.artist + self.band + "') ; ")
        conn.commit()