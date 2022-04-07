from distutils.log import debug
from flask import Flask, render_template, jsonify
import get_data
app = Flask(__name__)


@app.route("/")
def hello():
    #artists = get_data.get_all_artist()
    return render_template("base.html")


@app.route("/artist")
def display_artist():
    artists = get_data.get_all_artist()
    artist_arr = [{'id': i[0], 'name':i[1]}for i in artists]
    return jsonify(artist_arr)


@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs = get_data.get_all_songs(aid)
    artists = get_data.get_all_artist()
    artist = get_data.singer(aid)
    return render_template("songlist.html", artist=artist, artists=artists, songs=songs, current=aid)


@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid, aid):
    lyrics = get_data.get_lyrics(sid)
    songs = get_data.get_all_songs(aid)
    artists = get_data.get_all_artist()
    artist = get_data.singer(aid)
    return render_template("lyrics.html", lyrics=lyrics, artist=artist, artists=artists, songs=songs, current=aid, csong=sid)


if __name__ == "__main__":
    app.run(debug=True)
