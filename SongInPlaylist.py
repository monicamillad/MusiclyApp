import sqlite3

class songinplaylist:

    def __init__(self,song,playlist):
        self.song = song
        self.playlist = playlist


    def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("INSERT INTO songinplaylist (song,playlist,song_playlist) VALUES ( '"+self.song+"' , '"+self.playlist+"' , '"+self.song+self.playlist+"' ) ;")
         conn.commit()

    def DeleteSongFromPlaylist(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM songinplaylist WHERE( song_playlist = '" +self.song+self.playlist+"') ; ")
        conn.commit()

