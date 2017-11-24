import sqlite3

class playlist:
    num = 0
    def __init__(self,name="",description=""):
        self.name = name
        self.description = description
        self.songs = []
        playlist.num += 1

    def addToDatabase(self):
         conn = sqlite3.connect('MusiclyApp.db')
         conn.execute("INSERT INTO playlist (name,description) VALUES ('"+self.name+"', '"+self.description+"' ) ;")
         conn.commit()



    def DeletePlaylist(self):
        conn = sqlite3.connect('MusiclyApp.db')
        conn.execute("DELETE FROM songinplaylist WHERE playlist ='" + self.name + "'  ;")
        print(self.name)
        conn.execute("DELETE FROM playlist WHERE name ='" + self.name + "'  ;")
        conn.commit()
