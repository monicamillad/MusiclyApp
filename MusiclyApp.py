import sys
import sqlite3
import winsound

from PyQt4 import QtGui, QtCore

from PlayList import playlist
from Song import Song
from SongInPlaylist import  songinplaylist

conn =  sqlite3.connect('MusiclyApp.db')

conn.execute(''' CREATE TABLE if not exists playlist 
 (name TEXT PRIMARY KEY NOT NULL,
  description TEXT );''')

conn.execute(''' CREATE TABLE if not exists song
 (name TEXT PRIMARY KEY NOT NULL,
  date TEXT,
  genres TEXT,
  lyrics TEXT,
  lenght TEXT,
  path TEXT );''')

conn.execute(''' CREATE TABLE if not exists album
 (title TEXT PRIMARY KEY NOT NULL,
  bandname TEXT );''')

conn.execute(''' CREATE TABLE if not exists band
 (name TEXT PRIMARY KEY NOT NULL);''')

conn.execute(''' CREATE TABLE if not exists artist
 (name TEXT PRIMARY KEY NOT NULL,
  date TEXT );''')

conn.execute(''' CREATE TABLE if not exists artistinband
 (artist TEXT NOT NULL,
  band TEXT NOT NULL,
  artist_band PRIMARY KEY);''')

conn.execute(''' CREATE TABLE if not exists bandofthesong
 (song TEXT NOT NULL,
  band TEXT NOT NULL,
  song_band PRIMARY KEY);''')

conn.execute(''' CREATE TABLE if not exists featuredofthesong
 (song TEXT NOT NULL,
  featured TEXT NOT NULL,
  song_featured PRIMARY KEY);''')

conn.execute(''' CREATE TABLE if not exists songinplaylist
 (song TEXT NOT NULL,
  playlist TEXT NOT NULL,
  song_playlist PRIMARY KEY);''')

conn.commit()

# app = QtGui.QApplication(sys.argv)
# window = QtGui.QWidget()
# window.setGeometry(50,50,500,300)
# window.setWindowTitle("ashaf")
#
# window.show()
#
# sys.exit(app.exec_())


# p1 = playlist("playlist1","7mada")
# p1.addToDatabase()
#
# p2 = playlist("playlist2","3asalya")
# p2.addToDatabase()

# cursor = conn.execute("SELECT name from playlist")
#
#
# for row in cursor:
#     print(row[0])

# s = Song("Never meant to belong","","","","3:45","","")
# s.addToDatabase()

# sp = songinplaylist("Never meant to belong","playlist1")
# sp.addToDatabase()


# song = "Above_Beyond_-_We_were_in_heaven_you_and_I_.wav"

# when adding a new song in the playlist make sure that both are exisiting

#check if the album is exixt or not or it's a single song aslnnn

#check that the band is existing before adding artist in it


# pyuic4 -x PlaylistView.ui -o PlaylistView.py
