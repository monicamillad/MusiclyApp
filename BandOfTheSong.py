import sqlite3

class bandofthesong:

    def __init__(self,song,band):

        self.song = song
        self.band = band


    def addToDatabase(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("INSERT INTO bandofthesong (song,band,song_band) VALUES ( '" + self.song + "' , '" + self.band + "' , '" + self.song + self.band + "' ) ;")
        conn.commit()


    def DeleteSongFromBand(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM bandofthesong WHERE( song_band = '" + self.song + self.band + "') ; ")
        conn.commit()