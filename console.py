# Use this file to test your repository functions 
import pdb
from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist('Guns and Roses', 40)
artist_repository.save(artist_1)
artist_2 = Artist('Adele', 25)
artist_repository.save(artist_2)

album_1 = Album('First_album', 15, artist_1)
album_repository.save(album_1)

album_repository.select(album_1.id)
artist_repository.select(artist_1.id)
