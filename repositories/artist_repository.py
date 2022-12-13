from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING *"
    values = [artist.name, artist.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = 'DELETE FROM artists'
    run_sql(sql)

def select(id):
    artist = None
    sql = 'SELECT * FROM artists WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist (result['name'], result['age'], result['id'])
    return artist

def select_all():
    artists = []
    sql = 'SELECT * FROM albums'
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['age'], row['id'])
        artists.append(artist)
    return artists

