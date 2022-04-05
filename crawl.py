import requests
from bs4 import BeautifulSoup
import psycopg2
import sys

def get_artists(url):
    ret = []
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklist = soup.find("table", {"class": "tracklist"})
    links = tracklist.find_all("a")
    for i in links:
        ret.append((i.text, i['href']))
    return ret

def get_songs(artist_url):
    songs=[]
    r = requests.get(artist_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links=tracklists.find_all("a")
    for i in links:
        songs.append((i.text,i['href']))
    return songs

def get_lyrics(song_url):
    r = requests.get(song_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics

def crawl():
    conn = psycopg2.connect("dbname=Lyrics")
    cur = conn.cursor()
    cur.execute("CREATE TABLE artist ( id SERIAL PRIMARY KEY, name VARCHAR(20) );")
    cur.execute("CREATE TABLE song ( song_id SERIAL PRIMARY KEY, artist INTEGER references artist(id), song_name TEXT, lyrics TEXT );")
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists[:10]:
        cur.execute("INSERT INTO artist (name) VALUES (%s);", (name,))
        print(name, " : ",link)
        songs = get_songs(link)
        for song, song_link in songs[:10]:
                lyrics = get_lyrics(song_link)
                cur.execute("INSERT INTO song (artist, song_name, lyrics) VALUES ((SELECT id from artist where name=%s),%s,%s);", (name,song,lyrics))    
    conn.commit()
    print("DONE")

def get_all_songs(artist):
    conn = psycopg2.connect("dbname=Lyrics")
    cur = conn.cursor()
    cur.execute("SELECT song.song_name FROM song, artist WHERE artist.id = song.artist AND artist.name=%s", (artist,))
    songs = cur.fetchall()
    return songs



if __name__ == "__main__":
    crawl()