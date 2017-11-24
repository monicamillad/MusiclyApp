import sqlite3

class album:

    def __init__(self,title,bandname=""):
        self.title = title
        self.bandname = bandname
        self.songs = []

    def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("INSERT INTO album (title,bandname) VALUES ( '"+self.title+"' , '"+self.bandname+"' ) ;")
         conn.commit()


    def addSongToAlbum(self,song):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("UPDATE song SET album = '" + self.title + "' WHERE( name = '" + song + "' ) ; ")
         conn.commit()


    def DeleteAlbum(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("UPDATE song SET album = '' WHERE( album = '" + self.title + "' ) ; ")
        conn.execute("DELETE FROM album WHERE( title = '" + self.title + "' );" )
        conn.commit()