import sqlite3

from Band import band

class artist:

    def __init__(self,name,date=""):

        self.name = name
        self.dtae = date
        self.bands = []


    def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         b = band(self.name)
         b.addToDatabase()
         conn.execute("INSERT INTO artist (name,date) VALUES ( '"+self.name+"' , '"+self.date+"' ) ;")
         conn.commit()

    def DeleteArtist(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM artistinband WHERE( artist = '" + self.name + "') ; ")
        conn.execute("DELETE FROM band WHERE( name = '" + self.name + "') ; ")
        conn.execute("DELETE FROM artist WHERE( name = '" + self.name + "') ; ")
        conn.commit()