import sqlite3

class featuredofthesong:

    def __init__(self,song,featured):

        self.song = song
        self.featured = featured


    def addToDatabase(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("INSERT INTO bandofthesong (song,band,song_band) VALUES ( '" + self.song + "' , '" + self.featured + "' , '" + self.song + self.featured + "' ) ;")
        conn.commit()


    def DeleteSongFromBand(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM bandofthesong WHERE( song_featured = '" + self.song + self.featured + "') ; ")
        conn.commit()