import sqlite3

class band:

     def __init__(self,name):

         self.name = name
         self.artists = []
         self.songs = []

     def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("INSERT INTO band (name) VALUES ( '" + self.name + "' ) ;")
         conn.commit()

     def DeleteBand(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("DELETE FROM artistinband WHERE( band = '" + self.name + "') ; ")
         conn.execute("DELETE FROM bandofthesong WHERE( band = '" + self.name + "') ; ")
         conn.execute("DELETE FROM band WHERE( name = '" + self.name + "') ; ")
         conn.commit()