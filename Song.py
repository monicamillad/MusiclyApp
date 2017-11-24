import sqlite3

class Song:
    num = 0

    def __init__(self,name,date="",genres="",lyrics="",lenght="",album="",path=""):
        self.name = name
        self.date = date
        self.genres = genres
        self.lyrics = lyrics
        self.length = lenght
        Song.num += 1
        self.bands = []
        self.featured = []
        self.album = album
        self.path = path

    def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("INSERT INTO song (name,date,genres,lyrics,lenght,path) VALUES ( '"+self.name+"' , '"+self.date+"' , '" + self.genres+"','"+self.lyrics+"','"+self.length+"','"+self.path+"' ) ;")
         conn.commit()


    def DeleteSong(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM bandofthesong WHERE( song = '" + self.name + "') ; ")
        conn.execute("DELETE FROM songinplaylist WHERE( song = '" + self.name + "') ; ")
        conn.execute("DELETE FROM song WHERE( name = '" + self.name + "') ; ")
        conn.commit()